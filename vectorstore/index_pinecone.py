# agentiq/vectorstore/index_pinecone.py
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
import os

pinecone.init(api_key="your-pinecone-api-key", environment="us-west1-gcp")
index = pinecone.Index("agentiq-docs")
embeddings = OpenAIEmbeddings()

# Later used by LlamaIndex/LangChain for RAG
vectorstore = Pinecone(index, embeddings.embed_query, "text")
