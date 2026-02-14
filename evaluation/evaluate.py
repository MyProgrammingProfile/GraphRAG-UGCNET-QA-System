import json
import csv

from rag.answer_generator import generate_answer

# -----------------------------
# Load evaluation questions
# -----------------------------
with open("evaluation/questions_unit1_5.json", "r") as f:
    questions = json.load(f)

results = []

# -----------------------------
# Evaluation loop
# -----------------------------
for q in questions:
    question_text = q["question"]
    expected = q["expected_answer"]

    # -------- Baseline RAG (text only) --------
    baseline_docs = [
        "The spindle assembly checkpoint ensures correct chromosome attachment.",
        "Checkpoint failure results in chromosome missegregation."
    ]

    baseline_answer = baseline_docs[0]  # simulate text-only output

    baseline_correct = expected.lower() in baseline_answer.lower()

    # -------- Graph RAG (your system) --------
    graph_docs = baseline_docs
    graph_paths = ["Spindle assembly checkpoint → PREVENTS → Aneuploidy"]

    graph_answer, reasoning = generate_answer(
        question_text,
        graph_docs,
        graph_paths
    )

    graph_correct = expected.lower() in graph_answer.lower()
    reasoning_present = len(reasoning) > 0

    results.append({
        "question_id": q["id"],
        "question": question_text,
        "expected_answer": expected,
        "baseline_correct": baseline_correct,
        "graph_correct": graph_correct,
        "reasoning_present": reasoning_present
    })

# -----------------------------
# Save results
# -----------------------------
with open("evaluation/results.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=results[0].keys()
    )
    writer.writeheader()
    writer.writerows(results)

print("Evaluation completed. Results saved to evaluation/results.csv")
