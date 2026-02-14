import pickle
import networkx as nx

with open("kg/graphs/biological_kg.pkl", "rb") as f:
    G = pickle.load(f)

# find candidate source nodes containing keywords
source_candidates = [n for n in G.nodes if "spindle" in n.lower() and "checkpoint" in n.lower()]
target_candidates = [n for n in G.nodes if "aneuploidy" in n.lower()]

print("Source candidates:", source_candidates)
print("Target candidates:", target_candidates)

if not source_candidates or not target_candidates:
    print("No suitable source/target found.")
    exit()

source = source_candidates[0]
target = target_candidates[0]

if nx.has_path(G, source, target):
    path = nx.shortest_path(G, source, target)
    print("\nReasoning path:")
    for i in range(len(path) - 1):
        rel = G[path[i]][path[i+1]]["relation"]
        print(f"{path[i]} --{rel}--> {path[i+1]}")
else:
    print("No reasoning path found.")
