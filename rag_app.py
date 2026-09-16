import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from create_database import create_database

load_dotenv()

st.title("📚 PDF RAG Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully.")

    if st.button("Create Vector Database"):
        create_database("uploaded.pdf")
        st.success("Vector database created successfully!")

st.divider()

query = st.text_input("Ask a question about your document")

if query:

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10,
            "lambda_mult": 0.5
        }
    )

    llm = ChatGroq(
        model="openai/gpt-oss-20b"
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an helpful AI assistant. "
            "Use ONLY the provided context to answer the question. "
            "If the answer is not present in the context, "
            "say 'I could not find the answer in the document.'"
        ),
        (
            "human",
            "Context:\n{context}\n\nQuestion:\n{question}"
        )
    ])

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(final_prompt)

    st.write("### Answer")
    st.write(response.content)