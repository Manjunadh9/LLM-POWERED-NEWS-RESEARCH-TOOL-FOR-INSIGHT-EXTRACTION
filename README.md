# 🔬 AI News Research Tool

<div align="center">

![AI News Research Tool](https://img.shields.io/badge/AI-News%20Research-blue?style=for-the-badge&logo=artificial-intelligence)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google)](https://ai.google.dev)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-green?style=for-the-badge)](https://github.com/facebookresearch/faiss)

**🚀 AI-powered news article analysis and insight extraction using Google Gemini, FAISS vector search, and Streamlit**

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-reference)

</div>

---

## 🌟 **Overview**

Transform how you analyze news content with our AI-powered research tool. Process multiple news articles simultaneously, extract key insights, and get intelligent answers to your questions with source attribution.

### **🎯 What it does:**
- **Ingests** multiple news article URLs
- **Processes** content using advanced NLP techniques
- **Builds** semantic vector indexes for fast retrieval
- **Answers** questions using Google Gemini AI
- **Provides** source citations and content previews

---

## ✨ **Features**

### **🤖 AI-Powered Analysis**
- **Google Gemini Integration** - Multiple model fallback (Flash → Pro → 1.0)
- **Intelligent Q&A** - Context-aware responses with source attribution
- **Semantic Search** - FAISS-powered vector similarity matching
- **Rate Limit Handling** - Automatic optimization for API usage

### **📊 Content Processing**
- **Multi-URL Support** - Process 1-10 articles simultaneously  
- **Smart Chunking** - Optimized text splitting for better retrieval
- **Format Support** - HTML, text, and structured content parsing
- **Persistent Storage** - Local FAISS index for repeated queries

### **🎨 User Experience**
- **Modern UI** - Clean Streamlit interface with real-time feedback
- **Mobile Responsive** - Works seamlessly across all devices
- **Error Handling** - Graceful degradation and recovery
- **Progress Tracking** - Visual indicators for all operations

---

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.10+ (3.11 or 3.12 recommended)
- Google Gemini API Key ([Get yours here](https://makersuite.google.com/app/apikey))

### **Installation**

```bash
# Clone the repository
git clone https://github.com/Akshayvarma-9/ai-news-research-tool.git
cd ai-news-research-tool

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp config/.env.template config/.env
# Edit config/.env and add your GEMINI_API_KEY
```

### **Run Application**

```bash
# Option 1: Simple launcher
python run.py

# Option 2: Direct command
python -m streamlit run src/main.py --server.port 8501

# Option 3: PowerShell script (Windows)
./scripts/start_app.ps1
```

**🌐 Access:** http://localhost:8501

---

## 📖 **Usage Guide**

### **Step 1: Add Articles**
1. Set number of URLs (1-10) in the sidebar
2. Paste news article URLs in the input fields
3. Click **"Process URLs"** to build the knowledge base

### **Step 2: Ask Questions**
1. Type your question in the main input field
2. Get AI-powered answers with source citations
3. Explore expandable source previews

### **Step 3: Analyze Results**
- Review comprehensive AI responses
- Check source attributions and links
- Explore related content chunks

---

## 🏗️ **Project Structure**

```
ai-news-research-tool/
├── 📄 README.md              # Project documentation
├── 📦 requirements.txt       # Python dependencies  
├── 🚀 run.py                # Simple application launcher
├── 🙈 .gitignore            # Git ignore configuration
│
├── 📁 src/                  # 🎯 Core Application
│   └── main.py              # Main Streamlit application
│
├── 📁 config/               # ⚙️ Configuration
│   ├── .env                 # Environment variables (create this)
│   └── .env.template        # Environment template
│
├── 📁 utils/                # 🛠️ Utilities
│   └── rate_limit_helper.py # API rate limiting tools
│
├── 📁 scripts/              # 📜 Scripts
│   └── start_app.ps1        # PowerShell launcher
│
├── 📁 docs/                 # 📚 Documentation
│   └── README.md            # Detailed documentation
│
└── 📁 data/                 # 💾 Generated Data
    └── faiss_index/         # Vector index storage
```

---

## ⚙️ **Configuration**

### **Environment Variables**

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GEMINI_API_KEY` | Google Gemini API key | ✅ Yes | None |

### **Model Configuration**

```python
# Automatic model fallback hierarchy
models = [
    "gemini-1.5-flash",    # Fast, cost-effective
    "gemini-1.5-pro",      # High quality
    "gemini-1.0-pro"       # Stable fallback
]

# Optimized settings
chunk_size = 200           # Tokens per chunk
chunk_overlap = 40         # Overlap between chunks
temperature = 0.7          # Response creativity
max_tokens = 300           # Response length limit
```

---

## 🔧 **API Reference**

### **Core Components**

#### **Document Processing**
```python
# URL loading and content extraction
loader = UnstructuredURLLoader(urls=urls)
data = loader.load()

# Text chunking for optimal retrieval
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=40
)
docs = splitter.split_documents(data)
```

#### **Vector Search**
```python
# FAISS index creation
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local("data/faiss_index")

# Semantic search
retriever = vectorstore.as_retriever()
results = retriever.get_relevant_documents(query)
```

#### **AI Integration**
```python
# Google Gemini setup with fallback
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    max_tokens=300
)

# Q&A chain with sources
chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)
```

---

## 📊 **Performance & Limits**

### **Processing Metrics**
- **Article Processing**: ~2-5 seconds per article
- **Query Response**: ~1-3 seconds  
- **Memory Usage**: ~100-200MB
- **Storage**: ~1-5MB per 10 articles

### **API Limits (Free Tier)**
- **Requests**: 15/minute, 1,500/day
- **Input Tokens**: 50,000/minute, 15M/day
- **Optimization**: Automatic rate limiting and model fallback

---

## 🛠️ **Development**

### **Setup Development Environment**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run in development mode
streamlit run src/main.py --server.runOnSave true
```

### **Code Style**
- Follow PEP 8 standards
- Use type hints where applicable
- Add docstrings for functions
- Test with multiple article sources

---

## 🚨 **Troubleshooting**

### **Common Issues**

#### **❌ Missing API Key**
```
Missing GEMINI_API_KEY environment variable
```
**Solution**: Create `config/.env` with your API key and restart

#### **❌ Rate Limit Exceeded**
```
API Rate Limit Exceeded
```
**Solution**: Wait 1 minute or upgrade API plan

#### **❌ Port Already in Use**
```
Port 8501 is already in use
```
**Solution**: Use alternative port:
```bash
python -m streamlit run src/main.py --server.port 8502
```

### **Performance Tips**
- 🔥 Use smaller batches (3-5 URLs max)
- ⏱️ Wait between requests (free tier: 15/min)
- 📝 Keep questions concise to reduce token usage
- 🔄 Clear index (`data/faiss_index/`) to rebuild

---

## 🤝 **Contributing**

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### **How to Contribute**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### **Development Guidelines**
- Write clear commit messages
- Add tests for new features
- Update documentation as needed
- Follow existing code style

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **Google AI** - For Gemini API and advanced language models
- **Facebook Research** - For FAISS vector search library  
- **Streamlit** - For the amazing web framework
- **LangChain** - For LLM integration tools
- **FastEmbed** - For efficient embedding generation

---

## 📞 **Support**

- 📖 **Documentation**: Check the troubleshooting section above
- 🐛 **Bug Reports**: [Open an issue](https://github.com/Akshayvarma-9/ai-news-research-tool/issues)
- 💡 **Feature Requests**: [Start a discussion](https://github.com/Akshayvarma-9/ai-news-research-tool/discussions)
- 📧 **Contact**: [Your Email](mailto:your-email@example.com)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ using Google Gemini AI, FAISS, and Streamlit

[⬆ Back to Top](#-ai-news-research-tool)

</div>
#   a i - n e w s - r e s e a r c h - t o o l  
 # ai-news-research-tool
# LLM-POWERED-NEWS-RESEARCH-TOOL-FOR-INSIGHT-EXTRACTION
