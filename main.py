# main.py
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Initialize model and prompt once
model = OllamaLLM(model="llama3.2")

template = """
You are an assistant specialized in answering questions about Kuve, a customer support FAQ bot.
Make your answers short and precise.
Use the previous conversation and relevant information in the document to maintain context and provide helpful answers.

Conversation so far:
{history}

Relevant information:
{context}

User's question:
{question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def get_response(question: str, history: str) -> tuple[str, str]:
    """
    Handles a single chat turn:
    - Retrieves relevant context (from Chroma retriever)
    - Generates a model response with conversation context
    - Returns (response, updated_history)
    """

    # Retrieve relevant context
    retrieved_docs = retriever.invoke(question)

    # If retriever returns a list of Documents, convert to readable text
    if isinstance(retrieved_docs, list):
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    else:
        context = str(retrieved_docs)

    # Generate model response
    result = chain.invoke({
        "history": history,
        "context": context,
        "question": question
    })

    # Update conversation history
    updated_history = f"{history}\nUser: {question}\nAssistant: {result}\n"

    return result, updated_history
