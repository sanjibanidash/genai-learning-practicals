# from dotenv import load_dotenv
# from langchain.chat_models import init_chat_model
# from langchain_core.prompts import PromptTemplate

# load_dotenv()

# model = init_chat_model(
#     "gemini-3.6-flash",
#     model_provider="google_genai"
# )

# prompt = PromptTemplate(
#     template="Write a short summary about {topic}.",
#     input_variables=["topic"]
# )

# final_prompt = prompt.invoke({
#     "topic": "Generative AI"
# })

# response = model.invoke(final_prompt)

# print(response.content[0]["text"])

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate

load_dotenv()

# LangChain: creates our Gemini chat model
model = init_chat_model(
    "gemini-3.6-flash",
    model_provider="google_genai"
)

# LangChain: creates a reusable prompt
prompt = PromptTemplate(
    template="""
Extract useful information from the movie paragraph below.

Give me:
- Movie name
- Genre
- Cast
- A quick summary

Movie paragraph:
{paragraph}
""",
    input_variables=["paragraph"]
)

# Put our actual paragraph into {paragraph}
final_prompt = prompt.invoke({
    "paragraph": """
    Interstellar is a science-fiction film directed by Christopher Nolan.
    The story follows a group of astronauts who travel through a wormhole
    in search of a new home for humanity. The movie stars Matthew McConaughey,
    Anne Hathaway, Jessica Chastain and Michael Caine.
    """
})

# Send the completed prompt to Gemini
response = model.invoke(final_prompt)

print(response.content[0]["text"])