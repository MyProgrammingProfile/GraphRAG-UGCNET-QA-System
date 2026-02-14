import os
import spacy
import networkx as nx
from langchain_community.document_loaders import TextLoader

nlp = spacy.load("en_core_web_sm")
G = nx.Graph()

def chunk_text(text, chunk_size=5000):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

documents = []

for file in os.listdir("data"):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join("data", file), encoding="utf-8")
        documents.extend(loader.load())

print(f"Loaded {len(documents)} documents")

for doc in documents:
    chunks = chunk_text(doc.page_content)

    for chunk in chunks:
        spacy_doc = nlp(chunk)

        chunk_entities = [
            ent.text.strip()
            for ent in spacy_doc.ents
            if len(ent.text.strip()) > 2
        ]

        for ent in chunk_entities:
            G.add_node(ent)

        for i in range(len(chunk_entities)):
            for j in range(i + 1, len(chunk_entities)):
                G.add_edge(chunk_entities[i], chunk_entities[j])

print("Knowledge Graph constructed")
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

import pickle
with open("biological_knowledge_graph.gpickle", "wb") as f:
    pickle.dump(G, f)

print("Graph saved as biological_knowledge_graph.gpickle")

print("\nSample graph connections:")
for node in list(G.nodes)[:5]:
    print(node, "->", list(G.neighbors(node))[:5])
