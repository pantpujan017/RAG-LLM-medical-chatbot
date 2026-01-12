from dotenv import load_dotenv
import os
from src.helper import (load_pdf_file, filter_to_minimal_docs,
                        text_split, download_hugging_face_embeddings)
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

# ---------- env variables ----------
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GEMINI_API_KEY   = os.getenv("GEMINI_API_KEY")   

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEMINI_API_KEY"]   = GEMINI_API_KEY  

# ---------- data ingestion ----------
extracted_data = load_pdf_file(data="data/")
filter_data  = filter_to_minimal_docs(extracted_data)
text_chunks  = text_split(filter_data)
embeddings   = download_hugging_face_embeddings()

# ---------- Pinecone ----------
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

# ---------- store vectors ----------
PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    index_name=index_name,
)