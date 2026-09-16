from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel
from typing import Optional

load_dotenv()


class Movie(BaseModel):
    title: str
    genre: list[str]
    director: Optional[str] = None
    cast: list[str]
    rating: Optional[float] = None
    release_year: Optional[int] = None


model = ChatGroq(
    model="openai/gpt-oss-120b"
)

structured_model = model.with_structured_output(Movie)