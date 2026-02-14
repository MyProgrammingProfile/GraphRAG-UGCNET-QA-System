from typing import List, Tuple
from neo4j import GraphDatabase
import faiss
import numpy as np
import pickle

# -------------------------
# Neo4j connection
# -------------------------
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "your_password_here"  # same as Neo4j Desktop

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

# -------------------------
# Load FAISS index & docs
# -------------------------
FAISS_INDEX_PATH = "faiss_index/index.faiss"
DOC_STORE_PATH = "faiss_index/documents.pkl"

index = faiss.read_index(FAISS_INDEX_PATH)

with open(DOC_STORE_PATH, "rb") as f:
    documents = pickle.load(f)

# -------------------------
# 1. Graph traversal
# -------------------------
def get_graph_paths(concepts: List[str]) -> List[str]:
    paths = []

    query = """
    MATCH (a:Concept)-[r]->(b:Concept)
    WHERE a.name IN $concepts
    RETURN a.name AS source, type(r) AS relation, b.name AS target
    """

    with driver.session(database="ugcnet") as session:
        results = session.run(query, concepts=concepts)
        for record in results:
            paths.append(
                f"{record['source']} → {record['relation']} → {record['target']}"
            )

    return paths

# -------------------------
# 2. Vector retrieval (FAISS)
# -------------------------
def vector_search(query_embedding: np.ndarray, top_k: int = 5):
    D, I = index.search(query_embedding, top_k)
    return [documents[i] for i in I[0]]

# -------------------------
# 3. Hybrid retrieval
# -------------------------
def hybrid_retrieve(
    query_embedding: np.ndarray,
    extracted_concepts: List[str]
) -> Tuple[List[str], List[str]]:

    # Step A: graph reasoning
    graph_paths = get_graph_paths(extracted_concepts)

    # Step B: expand query using graph context
    expanded_concepts = extracted_concepts + [
        p.split(" → ")[-1] for p in graph_paths
    ]

    # Step C: vector search
    retrieved_docs = vector_search(query_embedding)

    return retrieved_docs, graph_paths
