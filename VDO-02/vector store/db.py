from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document


documents = [
    Document(
        page_content="Python is a programming language used for data science.",
        metadata={"source": "AI Book"}
    ),
    Document(
        page_content="Pandas is a Python library used for data analysis.",
        metadata={"source": "Data Science Book"}
    ),
    Document(
        page_content="Neural Networks are used in deep learning.",
        metadata={"source": "Deep Learning Book"}
    )
]


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    persist_directory="chroma_db"
)