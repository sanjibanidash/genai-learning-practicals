\# VDO 3 — Tools, AI Agents \& Runnables



This folder contains the practical implementations from VDO 3 of the Generative AI course.



The main focus of this video is understanding how LLMs can use external tools and how these tools can be combined to build AI agents.



\---



\## 📚 Topics Covered



\### 1. Custom Tools



Learned how to create custom tools using LangChain's `@tool` decorator.



Example:



```python

@tool

def get\_text\_length(text: str) -> int:

&#x20;   return len(text)

