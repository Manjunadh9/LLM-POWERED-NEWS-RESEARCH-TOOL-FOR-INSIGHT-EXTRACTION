# 🔬 LLM-Powered News Research Tool

> **AI-driven article analysis and insight extraction using Google Gemini, FAISS vector search, and Streamlit**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://langchain.com)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI-orange.svg)](https://ai.google.dev)

---

## 🚀 **Features**

### **Core Capabilities**
- 📰 **Multi-URL Processing** - Analyze 1-10 news articles simultaneously
- 🔍 **Vector Search** - FAISS-powered semantic search with FastEmbed embeddings
- 🤖 **AI Q&A** - Google Gemini AI with automatic model fallback
- 📊 **Source Attribution** - Expandable source previews with citations
- ⚡ **Rate Limiting** - Built-in API rate limit handling and optimization

### **Technical Stack**
- **Frontend**: Streamlit with modern UI
- **AI/ML**: Google Gemini (Flash/Pro), LangChain, FastEmbed
- **Vector DB**: FAISS with persistent storage
- **Processing**: Unstructured, BeautifulSoup, html2text

---

## 📋 **Quick Start**

### **1. Prerequisites**
- **Python 3.10-3.12** (recommended)
- **Google Gemini API Key** ([Get yours here](https://makersuite.google.com/app/apikey))

### **2. Installation**
```powershell
# Clone/navigate to project
cd "C:\Users\<your-username>\OneDrive\Documents\minor-2\Source Code"

# Install dependencies
pip install -r requirements.txt
```

### **3. Configuration**
Create `.env` file:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

### **4. Run Application**
```powershell
# Option 1: Using PowerShell script (Recommended)
.\start_app.ps1

# Option 2: Direct command
python -m streamlit run main.py --server.port 8501
```

**Access:** http://localhost:8501

---

## 🎯 **Usage Guide**

### **Step 1: Add Articles**
- Set number of URLs (1-10) in sidebar
- Paste news article URLs
- Click **"Process URLs"**

### **Step 2: Ask Questions**
- Type questions about processed content
- Get AI-powered answers with source citations
- View expandable source previews

### **Step 3: Analyze Results**
- Review AI responses with confidence scores
- Check source attributions
- Explore related content chunks

---

## 🛠️ **Project Structure**

```
Source Code/
├── main.py                 # 🎯 Main Streamlit application
├── start_app.ps1          # 🚀 PowerShell startup script
├── rate_limit_helper.py   # ⚡ API rate limit utilities
├── requirements.txt       # 📦 Python dependencies
├── .env                   # 🔐 Environment variables (create this)
├── .env.template         # 📝 Environment template
├── data/                 # 💾 Generated data storage
│   └── faiss_index/      # 🔍 Vector index files
└── venv/                 # 🐍 Virtual environment (optional)
```

---

## ⚙️ **Configuration**

### **Environment Variables**
| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | ✅ Yes |

### **Model Settings**
- **Primary**: `gemini-1.5-flash` (fast, cost-effective)
- **Fallback**: `gemini-1.5-pro` → `gemini-1.0-pro`
- **Chunk Size**: 200 tokens (optimized for rate limits)
- **Temperature**: 0.7 (balanced creativity)

---

## 🔧 **Troubleshooting**

### **Common Issues**

#### **❌ Missing API Key**
```
Missing GEMINI_API_KEY environment variable
```
**Solution**: Create `.env` file with your API key and restart

#### **❌ Unicode Decode Error**
```
UnicodeDecodeError: 'utf-8' codec can't decode
```
**Solution**: App has built-in fallback - refresh browser

#### **❌ Port Already in Use**
```
Port 8501 is already in use
```
**Solution**: Use alternative port:
```powershell
python -m streamlit run main.py --server.port 8502
```

#### **❌ Rate Limit Exceeded**
```
API Rate Limit Exceeded
```
**Solution**: Wait 1 minute or upgrade API plan

### **Performance Tips**
- 🔥 **Use smaller batches** (3-5 URLs max)
- ⏱️ **Wait between requests** (free tier: 15/min)
- 📝 **Shorter questions** reduce token usage
- 🔄 **Clear index** (`data/faiss_index/`) to rebuild

---

## 📊 **API Limits & Costs**

### **Free Tier Limits**
- **Requests**: 15/minute, 1,500/day
- **Tokens**: 50,000 input/minute, 15M/day

### **Optimization Features**
- ✅ Automatic model fallback
- ✅ Rate limit detection
- ✅ Token usage optimization
- ✅ Chunking size control

---

## 🚀 **Advanced Usage**

### **Custom Configuration**
Modify `main.py` for:
- **Different models**: Change `ChatGoogleGenerativeAI(model=...)`
- **Chunk sizes**: Adjust `chunk_size` and `chunk_overlap`
- **Temperature**: Modify `temperature` for creativity control

### **Batch Processing**
```python
# Process multiple article sets
# 1. Process first batch of URLs
# 2. Ask questions
# 3. Clear index: delete data/faiss_index/
# 4. Process next batch
```

---

## 📚 **Dependencies**

### **Core Libraries**
```txt
streamlit              # Web interface
langchain             # LLM framework
langchain-community   # Community integrations
langchain-google-genai # Google AI integration
faiss-cpu            # Vector search
fastembed            # Fast embeddings
```

### **Processing Libraries**
```txt
unstructured         # Document parsing
html2text           # HTML to text conversion
beautifulsoup4      # Web scraping
lxml                # XML/HTML parser
python-dotenv       # Environment management
```

---

## 🔐 **Security & Best Practices**

### **API Key Security**
- ✅ Use `.env` file (never commit to git)
- ✅ Keep API keys private
- ✅ Monitor usage and costs
- ✅ Rotate keys periodically

### **Data Privacy**
- 📁 Local vector storage (`data/faiss_index/`)
- 🔒 No data sent to external services (except Gemini API)
- 🗑️ Clear index to remove processed content

---

## 🎨 **Features Showcase**

### **Smart Processing**
- **Multi-format support**: HTML, text, structured content
- **Intelligent chunking**: Optimized for semantic search
- **Persistent storage**: FAISS index saved locally

### **AI-Powered Analysis**
- **Context-aware responses**: Understands article relationships
- **Source attribution**: Direct links to original content
- **Confidence scoring**: Transparent AI reasoning

### **User Experience**
- **Real-time feedback**: Processing status and progress
- **Error handling**: Graceful degradation and recovery
- **Mobile responsive**: Works on all devices

---

## 📈 **Performance Metrics**

- **Processing Speed**: ~2-5 seconds per article
- **Query Response**: ~1-3 seconds
- **Memory Usage**: ~100-200MB
- **Storage**: ~1-5MB per 10 articles

---

## 🤝 **Contributing**

### **Development Setup**
```powershell
# Create development environment
python -m venv venv
pip install -r requirements.txt

# Run in development mode
streamlit run main.py --server.runOnSave true
```

### **Code Style**
- Follow PEP 8 standards
- Use type hints where applicable
- Add docstrings for functions
- Test with multiple article sources

---

## 📞 **Support**

### **Getting Help**
- 📖 Check troubleshooting section above
- 🐛 Report issues with error logs
- 💡 Feature requests welcome
- 📧 Contact: [Your contact info]

### **Useful Links**
- [Google AI Studio](https://makersuite.google.com/app/apikey) - Get API key
- [Streamlit Docs](https://docs.streamlit.io) - Framework documentation
- [LangChain Docs](https://python.langchain.com) - LLM framework guide

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ using Google Gemini AI, LangChain, and Streamlit**
