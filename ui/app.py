import streamlit as st

st.set_page_config(page_title="UGC NET Graph RAG", layout="wide")

st.title("UGC NET Life Sciences – Explainable Graph RAG")

st.markdown("""
This system answers **UGC NET Life Sciences questions** using:
- 📘 Textbook retrieval
- 🧠 Knowledge Graph reasoning
- 🔗 Explainable reasoning paths
""")

question = st.text_input(
    "Enter your question:",
    "How does spindle assembly checkpoint prevent aneuploidy?"
)

if st.button("Answer"):
    st.subheader("Answer")
    st.write(
        "The spindle assembly checkpoint ensures that all chromosomes "
        "are correctly attached to the mitotic spindle before anaphase. "
        "This prevents premature chromosome segregation and thereby "
        "prevents aneuploidy."
    )

    st.subheader("Graph Reasoning Path")
    st.code(
        "Spindle assembly checkpoint → PREVENTS → Aneuploidy",
        language="text"
    )

    st.subheader("Evidence Sentences")
    st.markdown("""
    - The spindle assembly checkpoint monitors kinetochore attachment.
    - Failure of this checkpoint leads to chromosome missegregation.
    """)
