from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

response = model.invoke(
   "Explain machine learning to a 10-year-old in three sentences."
)

print(response.content)