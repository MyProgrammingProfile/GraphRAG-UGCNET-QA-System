import pickle
import networkx as nx

# Load existing graph using pickle
with open("biological_knowledge_graph.gpickle", "rb") as f:
    graph = pickle.load(f)

# Add nodes (concepts)
graph.add_node(
    "Cell cycle",
    entity_type="Process",
    unit="UNIT_III"
)

graph.add_node(
    "Spindle assembly checkpoint",
    entity_type="Checkpoint",
    unit="UNIT_III"
)

graph.add_node(
    "Aneuploidy",
    entity_type="Outcome",
    unit="UNIT_III"
)

# Add edges (relations)
graph.add_edge(
    "Spindle assembly checkpoint",
    "Aneuploidy",
    relation="prevents"
)

graph.add_edge(
    "Spindle assembly checkpoint",
    "Cell cycle",
    relation="regulates"
)

# Save updated graph using pickle
with open("biological_knowledge_graph.gpickle", "wb") as f:
    pickle.dump(graph, f)

print("UNIT III concepts and relations added successfully.")