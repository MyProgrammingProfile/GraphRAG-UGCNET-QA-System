def build_prompt(question, retrieved_docs, graph_paths):
    prompt = f"""
You are answering a UGC NET Life Sciences question.

Question:
{question}

Relevant biological reasoning paths:
"""
    for path in graph_paths:
        prompt += f"- {path}\n"

    prompt += "\nSupporting textbook information:\n"
    for doc in retrieved_docs:
        prompt += f"- {doc}\n"

    prompt += """
Answer concisely, scientifically, and at UGC NET level.
Explain causality clearly.
"""

    return prompt


def generate_answer(question, retrieved_docs, graph_paths):
    prompt = build_prompt(question, retrieved_docs, graph_paths)

    # 🔹 For now (no LLM call yet)
    # We simulate final answer using retrieved knowledge
    answer = (
        "Failure of the spindle assembly checkpoint leads to improper chromosome "
        "segregation during mitosis or meiosis, resulting in aneuploidy."
    )

    return answer, graph_paths
