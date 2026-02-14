import pickle

# Load graph
with open("biological_knowledge_graph.gpickle", "rb") as f:
    graph = pickle.load(f)

def answer_with_graph(question: str):
    question = question.lower()

    if "spindle" in question:
        node = "Spindle assembly checkpoint"
    else:
        return "Question not covered by current graph."

    answers = []

    for neighbor in graph.successors(node):
        relation = graph[node][neighbor].get("relation", "related_to")
        answers.append(f"{relation} {neighbor}")

    if not answers:
        return "No graph-based answer found."

    explanation = (
        f"Based on the knowledge graph, the {node} "
        f"{', and '.join(answers)}."
    )

    return explanation


if __name__ == "__main__":
    q = "Failure of spindle assembly checkpoint leads to what?"
    print("Q:", q)
    print("A:", answer_with_graph(q))
