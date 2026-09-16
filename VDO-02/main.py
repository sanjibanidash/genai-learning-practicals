from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Load existing vector database
vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)


# MMR Retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)


# LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b"
)


# Prompt
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


print("RAG SYSTEM CREATED")
print("PRESS 0 TO EXIT")


while True:
    query = input("You: ")

    if query == "0":
        break

    docs = retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(final_prompt)

    print("\nAI:", response.content)
    print()