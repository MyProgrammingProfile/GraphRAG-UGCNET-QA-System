import pickle
import networkx as nx

# Load existing (undirected) graph
with open("biological_knowledge_graph.gpickle", "rb") as f:
    old_graph = pickle.load(f)

# Convert to directed graph
directed_graph = nx.DiGraph()

# Copy nodes with attributes
for node, attrs in old_graph.nodes(data=True):
    directed_graph.add_node(node, **attrs)

# Copy edges with attributes
for u, v, attrs in old_graph.edges(data=True):
    directed_graph.add_edge(u, v, **attrs)

# Save directed graph
with open("biological_knowledge_graph.gpickle", "wb") as f:
    pickle.dump(directed_graph, f)

print("Graph successfully converted to Directed Graph (DiGraph).")
