```markdown
# 🏥 Medical-Bot RAG Chat  
AI-powered medical Q&A assistant built with **Flask**, **Pinecone**, **Groq LLM** and **Hugging-Face embeddings**.  
Ask any health-related question and get instant, evidence-based answers retrieved from trusted medical PDFs.

![Chat UI](Screenshot%202026-01-12%20185222.png)

## ✨ Features
- **Retrieval-Augmented Generation** (RAG) – answers grounded in your own medical documents  
- **Fast, free LLM** via Groq (`llama-3.1-8b-instant`)  
- **Vector search** with Pinecone for sub-second similarity lookup  
- **Responsive web UI** – works on desktop & mobile

## 🚀 Run locally
```bash
pip install -r requirements.txt
python app.py        # http://localhost:8080
```

## 🐳 Docker one-liner
```bash
docker build -t medical-bot .
docker run -p 8080:8080 \
  -e PINECONE_API_KEY=<your-key> \
  -e GROQ_API_KEY=<your-key> \
  medical-bot
```

## 🔐 Required environment variables
| Variable | Purpose |
|----------|---------|
| `PINECONE_API_KEY` | Vector index access |
| `GROQ_API_KEY` | Free LLM inference |

## 📁 Project structure
```
├── data/                 # drop PDFs here before indexing
├── src/                  # helper & prompt modules
├── store_index.py        # build & upload embeddings
├── app.py                # Flask chat server
├── requirements.txt
├── Dockerfile
└── README.md
```

