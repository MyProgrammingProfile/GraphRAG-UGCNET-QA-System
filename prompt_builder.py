def build_graph_rag_prompt(question, retrieved_docs, graph_entities):
    context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    graph_context = "\n".join(graph_entities)

    prompt = f"""
You are an expert biology tutor for UGC NET Life Sciences.

Use the following information to answer the question.

Retrieved Text:
{context}

Biological Concept Relations (from Knowledge Graph):
{graph_context}

Question:
{question}

Provide a clear, concise, and conceptually correct answer.
"""
    return prompt
