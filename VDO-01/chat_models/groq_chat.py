from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b"
)

response = model.invoke(
    "Give me a short paragraph explaining machine learning."
)

print(response.content)