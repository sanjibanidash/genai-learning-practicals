from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = init_chat_model(
    "gemini-3.6-flash",
    model_provider="google_genai"
)

messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="What is machine learning?")
]

response = model.invoke(messages)

print("Response type:", type(response))
print("Response:", response)
print("Content:", response.content[0]["text"])