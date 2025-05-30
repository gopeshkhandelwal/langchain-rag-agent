
from langchain.prompts import PromptTemplate

def get_custom_rag_prompt():
    return PromptTemplate(
        input_variables=["context", "question"],
        template=""""
You are a knowledgeable AI assistant. Use the context below to answer the user's question.
Even if the context is incomplete, attempt a clear and informative response using your understanding.

Context:
{context}

Question:
{question}

Answer in a concise and helpful way:
""".strip()
    )
