import os
import requests

from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()


# ============================================================
# WEATHER TOOL
# ============================================================

@tool
def get_weather(city: str) -> str:
    """Get the current weather information for a city."""

    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return "OpenWeather API key is missing."

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    data = response.json()

    if response.status_code != 200:
        return f"Weather API error {response.status_code}: {data}"

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"Weather in {city}: {description}, {temperature}°C"


# ============================================================
# NEWS TOOL
# ============================================================

@tool
def search_city_news(city: str) -> str:
    """Search for the latest news about a city."""

    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        return "Tavily API key is missing."

    url = "https://api.tavily.com/search"

    payload = {
        "api_key": api_key,
        "query": f"latest news about {city}",
        "search_depth": "advanced",
        "max_results": 5
    }

    response = requests.post(
        url,
        json=payload
    )

    data = response.json()

    if response.status_code != 200:
        return f"News API error {response.status_code}: {data}"

    results = data.get("results", [])

    if not results:
        return f"No recent news found for {city}."

    news = []

    for result in results:

        title = result.get("title", "")
        content = result.get("content", "")

        news.append(
            f"{title}: {content}"
        )

    return "\n".join(news)


# ============================================================
# LLM
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


# ============================================================
# CREATE AGENT
# ============================================================

agent = create_agent(
    model=llm,
    tools=[
        get_weather,
        search_city_news
    ]
)


# ============================================================
# RUN AGENT
# ============================================================

if __name__ == "__main__":

    query = input("You: ")

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    print("\nCITY INTELLIGENCE AGENT:")

    final_message = result["messages"][-1]

    if isinstance(final_message.content, list):
        print(final_message.content[0]["text"])
    else:
        print(final_message.content)