# agentiq/vectorstore/index_pinecone.py

from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv
import pinecone
import os

# Load environment variables from .env
load_dotenv()

# Retrieve Pinecone credentials
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV", "us-west1-gcp")

if not pinecone_api_key:
    raise ValueError("PINECONE_API_KEY not set in environment.")

pinecone.init(api_key=pinecone_api_key, environment=pinecone_env)

index = pinecone.Index("agentiq-docs")
embeddings = OpenAIEmbeddings()

# Vector store for RAG
vectorstore = Pinecone(index, embeddings.embed_query, "text")
