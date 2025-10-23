# 🔬 LLM-Powered News Research Tool

<div align="center">

![LLM News Tool](https://img.shields.io/badge/LLM-News%20Research-blue?style=for-the-badge\&logo=artificial-intelligence)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge\&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit)](https://streamlit.io)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-green?style=for-the-badge)](https://github.com/facebookresearch/faiss)

**🚀 LLM-powered news article analysis and insight extraction using FAISS vector search and Streamlit**

[Demo](#-demo) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-reference)

</div>

---

## 🌟 **Overview**

Analyze news content intelligently with your own LLM-powered research tool. Process multiple news articles, extract key insights, and get answers to questions with source attribution.

### **🎯 What it does:**

* **Ingests** multiple news article URLs
* **Processes** content using advanced NLP and embeddings
* **Builds** semantic vector indexes for fast retrieval
* **Answers** questions using your chosen LLM
* **Provides** source citations and previews

---

## ✨ **Features**

### **🤖 LLM-Powered Analysis**

* **Custom LLM Integration** - Use OpenAI, local LLM, or other APIs
* **Intelligent Q&A** - Context-aware responses with sources
* **Semantic Search** - FAISS-powered vector similarity
* **Rate Limit Handling** - Automatic API usage optimization

### **📊 Content Processing**

* **Multi-URL Support** - Process multiple articles
* **Smart Chunking** - Optimized text splitting
* **Format Support** - HTML and text parsing
* **Persistent Storage** - FAISS index for repeated queries

### **🎨 User Experience**

* **Streamlit UI** - Clean, interactive interface
* **Mobile-Friendly** - Works across devices
* **Error Handling** - Graceful recovery
* **Progress Tracking** - Visual indicators

---

## 🚀 **Quick Start**

### **Prerequisites**

* Python 3.10+
* LLM API key (OpenAI, Google Gemini, or any LLM)
* Streamlit installed

### **Installation**

```bash
# Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp config/.env.template config/.env
# Edit config/.env and add your API keys
```

### **Run Application**

```bash
# Simple launcher
python run.py

# Or direct Streamlit launch
python -m streamlit run src/main.py --server.port 8501
```

**🌐 Access:** [http://localhost:8501](http://localhost:8501)

---

## 📖 **Usage Guide**

### **Step 1: Add Articles**

1. Paste article URLs
2. Click **Process URLs** to build the knowledge base

### **Step 2: Ask Questions**

1. Type a query
2. Get LLM-powered answers with sources

### **Step 3: Analyze Results**

* Review answers and source links
* Explore related content chunks

---

## 🏗️ **Project Structure**

```
llm-news-research-tool/
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── run.py                     # Application launcher
├── .gitignore                 # Git ignore config

├── src/                       # Core Application
│   └── main.py                # Streamlit interface

├── config/                    # Configuration
│   └── .env                   # Environment variables

├── utils/                     # Utilities
│   └── rate_limit_helper.py   # Optional API helper

├── data/                      # Generated Data
│   └── faiss_index/           # FAISS index storage
```

---

## ⚙️ **Configuration**

| Variable      | Description          | Required |
| ------------- | -------------------- | -------- |
| `LLM_API_KEY` | API key for your LLM | ✅ Yes    |

---

## 🔧 **API Reference**

### **Document Processing**

```python
# Load article content
loader = UnstructuredURLLoader(urls=urls)
docs = loader.load()
```

### **Vector Search**

```python
# FAISS index creation
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local("data/faiss_index")
```

### **LLM Integration**

```python
# Example: OpenAI / custom LLM
llm = YourLLM(api_key=LLM_API_KEY)
chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)
```

---

## 📄 **License**

This project is licensed under the MIT License.

---

## 🙏 **Acknowledgments**

* **FAISS** – Vector similarity search
* **Streamlit** – Web UI framework
* **LangChain** – LLM integration tools

---

## 📞 **Support**

* 🐛 Bug reports: [GitHub Issues](https://github.com/Manjunadh9/LLM-POWERED-NEWS-RESEARCH-TOOL-FOR-INSIGHT-EXTRACTION/issues)
* 💡 Feature requests: [GitHub Discussions](https://github.com/Manjunadh9/LLM-POWERED-NEWS-RESEARCH-TOOL-FOR-INSIGHT-EXTRACTION/discussions)

---

<div align="center">

**⭐ Star this repository if it helps you!**

Made with ❤️ using LLM, FAISS, and Streamlit

[⬆ Back to Top](#-llm-powered-news-research-tool)

</div>

---

I left placeholders like `Manjunadh9` and `LLM-POWERED-NEWS-RESEARCH-TOOL-FOR-INSIGHT-EXTRACTION`  
