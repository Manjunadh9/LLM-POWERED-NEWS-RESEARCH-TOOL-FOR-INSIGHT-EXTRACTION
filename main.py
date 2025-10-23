import os
import streamlit as st
import pickle
import time
import re
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Try to load environment variables, fallback if .env file has issues
try:
    load_dotenv()
except UnicodeDecodeError:
    st.warning("⚠️ .env file encoding issue - using fallback method")

st.title("Article Research Tool 📈")
st.sidebar.title("News Article URLs")

# Check for Gemini API key early and show a clear message
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBibJIN4dRvYvBs_ET7-tPMhaLV01eTkeo").strip()
if not GEMINI_API_KEY:
    st.error("❌ Missing GEMINI_API_KEY")
    st.info("""
    **To fix this:**
    1. Create a `.env` file in this directory
    2. Add: `GEMINI_API_KEY=your_actual_api_key_here`
    3. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
    4. Restart the app
    """)
    st.stop()

# User selects the number of URLs they want to input
num_urls = st.sidebar.number_input("How many URLs?", min_value=1, max_value=10, value=3, step=1)

urls = []
for i in range(num_urls):
    url = st.sidebar.text_input(f"URL {i+1}", placeholder="https://example.com/article")
    if url.strip():  # Only add non-empty URLs
        urls.append(url)

# Show URL count
if urls:
    st.sidebar.success(f"📝 {len(urls)} URL(s) ready to process")

process_url_clicked = st.sidebar.button("Process URLs")
# Use a folder for FAISS persistent storage under data/
index_dir = "data/faiss_index"

# Show index status
if os.path.exists(index_dir):
    st.sidebar.info("📚 Index available - Ready for questions!")
else:
    st.sidebar.warning("⚠️ No index found - Process URLs first")

# Rate limiting info
st.sidebar.info("""
📊 **API Usage Tips:**
• Free tier: 15 req/min
• Use smaller text chunks
• Wait between requests
• Consider upgrading plan
""")

# Initialize embedding model (FastEmbed, CPU-only)
embeddings = FastEmbedEmbeddings()

# Initialize Gemini LLM with rate limiting and fallback
def get_llm():
    """Get LLM with rate limiting and fallback models"""
    models_to_try = [
        "gemini-1.5-flash",      # Faster, more cost-effective
        "gemini-1.5-pro",        # Higher quality but more expensive
        "gemini-1.0-pro"         # Fallback option
    ]
    
    for model in models_to_try:
        try:
            llm = ChatGoogleGenerativeAI(
                model=model,
                temperature=0.7,  # Reduced for more focused responses
                max_tokens=300,   # Reduced to save tokens
                google_api_key=GEMINI_API_KEY
            )
            st.sidebar.success(f"✅ Using {model}")
            return llm
        except Exception as e:
            if "quota" in str(e).lower() or "rate_limit" in str(e).lower():
                st.sidebar.warning(f"⚠️ Rate limit hit for {model}, trying next...")
                continue
            else:
                st.sidebar.success(f"✅ Using {model}")
                return llm
    
    # If all models fail, return the first one and let it error
    st.sidebar.error("❌ All models hit rate limits. Please wait and try again.")
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        max_tokens=300,
        google_api_key=GEMINI_API_KEY
    )

llm = get_llm()

if process_url_clicked:
    if not urls:
        st.error("Please enter at least one valid URL")
    else:
        try:
            # Load data
            loader = UnstructuredURLLoader(urls=urls)
            st.info("🔄 Loading data from URLs...")
            data = loader.load()
            
            if not data:
                st.error("No content could be extracted from the provided URLs")
            else:
                # Split data with smaller chunks to reduce token usage
                text_splitter = RecursiveCharacterTextSplitter(
                    separators=['\n\n', '\n', '.', ','],
                    chunk_size=200,  # Smaller chunks to reduce token consumption
                    chunk_overlap=40  # Reduced overlap to save tokens
                )
                st.info("✂️ Splitting text into chunks...")
                docs = text_splitter.split_documents(data)
                
                if not docs:
                    st.error("No text content could be extracted from the URLs")
                else:
                    # Create embeddings and save to FAISS index
                    vectorstore = FAISS.from_documents(docs, embeddings)
                    st.info("🔍 Building vector embeddings...")
                    time.sleep(1)

                    # Persist FAISS index without pickling embedding sessions
                    os.makedirs(index_dir, exist_ok=True)
                    vectorstore.save_local(index_dir)
                    st.success("✅ URLs processed successfully! You can now ask questions.")
        except Exception as e:
            st.error(f"Error processing URLs: {str(e)}")

# Question input section
st.header("Ask Questions")
query = st.text_input("Question: ", placeholder="Ask a question about the processed articles...")

if query:
    if os.path.exists(index_dir):
        try:
            with st.spinner("🔍 Searching for answers..."):
                vectorstore = FAISS.load_local(index_dir, embeddings, allow_dangerous_deserialization=True)
                chain = RetrievalQA.from_chain_type(
                    llm=llm, 
                    chain_type="stuff", 
                    retriever=vectorstore.as_retriever(),
                    return_source_documents=True
                )
                result = chain.invoke({"query": query})
            
            # Display answer
            st.header("Answer")
            st.write(result["result"])
            
            # Display sources if available
            source_docs = result.get("source_documents", [])
            if source_docs:
                st.subheader("Sources:")
                for i, doc in enumerate(source_docs):
                    source_url = doc.metadata.get('source', 'Unknown source')
                    st.write(f"• **Source {i+1}:** {source_url}")
                    with st.expander(f"Preview {i+1}"):
                        st.write(doc.page_content[:200] + "...")
        except Exception as e:
            error_msg = str(e)
            
            if "quota" in error_msg.lower() or "rate_limit" in error_msg.lower():
                st.error("❌ API Rate Limit Exceeded")
                st.info("""
                **You've hit Gemini API rate limits. Here are your options:**
                
                1. **Wait and retry** - Rate limits reset every minute
                2. **Use a different model** - The app will automatically try alternatives
                3. **Check your usage** - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
                4. **Upgrade plan** - Consider upgrading from free tier for higher limits
                
                **Current limits (Free Tier):**
                - 15 requests per minute
                - 1,500 requests per day
                - 50,000 input tokens per minute
                """)
                
                # Show countdown timer
                if "retry_delay" in error_msg:
                    delay_match = re.search(r'retry_delay\s*{\s*seconds:\s*(\d+)', error_msg)
                    if delay_match:
                        delay_seconds = int(delay_match.group(1))
                        st.warning(f"⏰ Wait {delay_seconds} seconds before retrying")
                
            elif "model_not_found" in error_msg.lower():
                st.error("❌ Model not available")
                st.info("💡 The app will automatically try alternative models.")
                
            else:
                st.error(f"❌ Error processing question: {error_msg}")
                st.info("💡 Try processing URLs again if the index seems corrupted.")
    else:
        st.warning("⚠️ Please process some URLs first before asking questions")


# To run the app:
# streamlit run main.py
# or
# python -m streamlit run main.py