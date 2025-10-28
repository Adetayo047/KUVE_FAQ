from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

# === CONFIG ===
DATA_FILE = "getkuve_faq.txt"  # or .txt file
DB_LOCATION = "./chroma_langchain_db"
COLLECTION_NAME = "KUVE_FAQ"

# === EMBEDDINGS ===
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# === Check if DB already exists ===
add_documents = not os.path.exists(DB_LOCATION)
documents = []
ids = []

if add_documents:
    print(f"Loading data from: {DATA_FILE}")

    # --- Load from CSV ---
    if DATA_FILE.endswith(".csv"):
        df = pd.read_csv(DATA_FILE)

        for i, row in df.iterrows():
            content = f"{row.get('Title', '')} {row.get('Review', '')}"
            metadata = {
                "rating": row.get("Rating", None),
                "date": row.get("Date", None),
            }
            documents.append(Document(page_content=content.strip(), metadata=metadata))
            ids.append(str(i))

    # --- Load from TXT ---
    elif DATA_FILE.endswith(".txt"):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Each line becomes one Document
        for i, line in enumerate(lines):
            if line.strip():  # ignore empty lines
                documents.append(Document(page_content=line.strip(), metadata={"source": DATA_FILE}))
                ids.append(str(i))
    else:
        raise ValueError("Unsupported file format. Please use .csv or .txt")

# === Initialize vector store ===
vector_store = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory=DB_LOCATION,
    embedding_function=embeddings,
)

# === Add documents if new ===
if add_documents and documents:
    vector_store.add_documents(documents=documents, ids=ids)
    print(f"✅ Added {len(documents)} documents to Chroma database.")
else:
    print("✅ Using existing Chroma database.")

# === Retriever for external use ===
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
