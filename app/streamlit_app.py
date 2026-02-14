import streamlit as st
from rag.hybrid_graph_rag import hybrid_answer

st.set_page_config(page_title="UGC NET GraphRAG", layout="centered")

st.title("UGC NET Life Sciences – GraphRAG Demo")

st.markdown(
    """
This application demonstrates a **GraphRAG system** where  
a **knowledge graph guides reasoning** before answer generation.
"""
)

question = st.text_input(
    "Enter a UGC NET–style question:",
    "Failure of spindle assembly checkpoint leads to what?"
)

if st.button("Get Answer"):
    answer, reasoning_path = hybrid_answer(question)

    st.subheader("Answer")
    st.success(answer)

    st.subheader("Graph Reasoning Path")
    for step in reasoning_path:
        st.code(step)
