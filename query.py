from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from entity_extractor import extract_entities_from_chunks
from graph_engine import load_graph, expand_entities

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
G = load_graph()

print("Graph RAG Ready. Type a question.\n")

while True:
    query = input("Ask a question: ")
    if query.lower() == "exit":
        break

    retrieved_docs = vectorstore.similarity_search(query, k=4)

    entities = extract_entities_from_chunks(retrieved_docs)
    expanded = expand_entities(entities, G)

    print("\nRetrieved Entities:", entities)
    print("Graph Expanded Entities:", expanded[:20])
