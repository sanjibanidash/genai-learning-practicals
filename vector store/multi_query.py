from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_groq import ChatGroq

load_dotenv()


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)


retriever = vectorstore.as_retriever()


llm = ChatGroq(
    model="openai/gpt-oss-20b"
)


multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=retriever,
    llm=llm
)


query = "What is gradient descent?"

docs = multi_query_retriever.invoke(query)


for d in docs:
    print(d.page_content)