
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from agent_app.prompts import get_custom_rag_prompt
from agent_app.config import get_llm
from langchain.tools import tool
import os

INDEX_DIR = "vectorstore/faiss_index"
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Safe loading — fail early if index is missing
if not os.path.exists(INDEX_DIR):
    raise FileNotFoundError(f"FAISS index not found at {INDEX_DIR}. Run `build_vectorstore.py` first.")

vectorstore = FAISS.load_local(INDEX_DIR, embedding_model, allow_dangerous_deserialization=True)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

rag_chain = RetrievalQA.from_chain_type(
    llm=get_llm(),
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": get_custom_rag_prompt()}
)

@tool
def DocumentQA(question: str) -> str:
    """Use only for answering questions based on internal file-based documents. Do not use for general knowledge or weather queries."""
    result = rag_chain.invoke({"query": question})
    answer = result.get("result", "") if isinstance(result, dict) else result
    answer = answer.strip().replace('"', '')
    print("🔍 RAG result:", answer)
    return answer
