# VDO-01 — Generative AI Fundamentals

This folder contains practical implementations covering the fundamentals of working with **LangChain, LLMs, prompts, structured output, Pydantic, and Streamlit**.

---

## 🎯 What I Learned

- How to connect an application with an LLM using LangChain
- How to initialize chat models using `init_chat_model`
- How to work with different LLM providers
- How to send messages to a chat model
- How to use `PromptTemplate`
- How to create structured outputs from an LLM
- How to define structured schemas using Pydantic
- How to use `with_structured_output()`
- How to build a simple Streamlit application around an LLM

---

## 🧠 Concepts Covered

### 1. Chat Models

Worked with chat models using LangChain and Gemini/Groq.

Example workflow:

```text
User Input
    ↓
Chat Model
    ↓
LLM Response
    ↓
response.content