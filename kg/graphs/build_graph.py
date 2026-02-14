import networkx as nx
import pickle
from pathlib import Path

RELATIONS_FILE = Path("kg/relation_extraction/relations.txt")
GRAPH_FILE = Path("kg/graphs/biological_kg.pkl")

G = nx.DiGraph()

with open(RELATIONS_FILE, "r", encoding="utf-8") as f:
    for line in f:
        parts = [x.strip() for x in line.split("|")]
        if len(parts) != 3:
            continue
        head, rel, tail = parts
        if head and rel and tail:
            G.add_node(head)
            G.add_node(tail)
            G.add_edge(head, tail, relation=rel)

with open(GRAPH_FILE, "wb") as f:
    pickle.dump(G, f)

print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
print(f"Graph saved to {GRAPH_FILE}")
