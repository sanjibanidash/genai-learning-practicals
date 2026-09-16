from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()


# Components
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

parser = StrOutputParser()


# Two different prompts
short_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 1-2 lines"
)

detailed_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detail"
)


# Runnable Parallel
chain = RunnableParallel({
    "short": short_prompt | model | parser,
    "detailed": detailed_prompt | model | parser
})


# Run the chain
result = chain.invoke({
    "topic": "Machine Learning"
})


print(result)