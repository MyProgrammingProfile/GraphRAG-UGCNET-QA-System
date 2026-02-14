import pickle
import networkx as nx

# Load the graph
with open("biological_knowledge_graph.gpickle", "rb") as f:
    graph = pickle.load(f)

node = "Spindle assembly checkpoint"

print(f"\nQuerying graph for: {node}\n")

# Outgoing relations
for neighbor in graph.successors(node):
    relation = graph[node][neighbor].get("relation", "related_to")
    print(f"{node} --{relation}--> {neighbor}")
