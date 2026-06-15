import streamlit as st
import os

from create_db import create_database
from main import ask_question


st.set_page_config(
    page_title="Smart RAG Assistant",
    page_icon="📚",
    layout="wide"
)


if "db_created" not in st.session_state:
    st.session_state.db_created = False

if "messages" not in st.session_state:
    st.session_state.messages = []


st.title("Smart RAG Knowledge Assistant")

st.caption("Upload a PDF and ask questions about it.")


with st.sidebar:

    st.header("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file:

        os.makedirs(
            "document_loaders",
            exist_ok=True
        )

        file_path = os.path.join(
            "document_loaders",
            uploaded_file.name
        )

        with open(
            file_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        if st.button("Create Knowledge Base"):

            with st.spinner("Processing PDF..."):

                create_database(file_path)

            st.session_state.db_created = True

            st.success("Knowledge base created successfully")

    st.divider()

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()


if not st.session_state.db_created:

    st.info("Upload a PDF and create the knowledge base.")

else:

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):

            st.write(msg["content"])

    question = st.chat_input(
        "Ask a question about the PDF..."
    )

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        answer = ask_question(question)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()