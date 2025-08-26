from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import os

# Set your OpenAI API Key
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

# Step 1: Load text documents (you can extend this to PDFs, etc.)
loader = TextLoader("C:/Users/sanat/LangGraph-Udemy-Course/LangGraphDHS/policies.txt")  # 🔁 Replace with your own policy file
documents = loader.load()

# Step 2: Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
docs = splitter.split_documents(documents)

# Step 3: Embed and create FAISS index
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs, embedding)

# Step 4: Save index locally
vectorstore.save_local("policy_faiss_index")

print("✅ FAISS index created and saved as 'policy_faiss_index'")
