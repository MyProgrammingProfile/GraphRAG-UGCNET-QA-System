import networkx as nx
import pickle

def load_graph(path="biological_knowledge_graph.gpickle"):
    with open(path, "rb") as f:
        G = pickle.load(f)
    return G

def expand_entities(entities, G, depth=1):
    expanded = set(entities)
    for ent in entities:
        if ent in G:
            neighbors = list(G.neighbors(ent))
            expanded.update(neighbors[:10])
    return list(expanded)
