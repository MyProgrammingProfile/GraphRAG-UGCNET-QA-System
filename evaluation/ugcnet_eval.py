import sys
import os

print("=== Evaluation script started ===")

# Force project root onto Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("Project root:", PROJECT_ROOT)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

print("Python path:")
for p in sys.path:
    print(" ", p)

from rag.hybrid_graph_rag import hybrid_answer

ugcnet_pyqs = [
    "Failure of spindle assembly checkpoint leads to what?",
    "What is the role of spindle assembly checkpoint in mitosis?"
]

print("\nUGC NET Life Sciences – GraphRAG Evaluation\n")

for q in ugcnet_pyqs:
    answer, reasoning = hybrid_answer(q)

    print("Q:", q)
    print("Answer:", answer)
    print("Reasoning Path:")
    for r in reasoning:
        print("  ", r)
    print("-" * 50)
