import streamlit as st
from langchain_openai import ChatOpenAI

def activity_agent(weather, time_available, preference):
    llm = ChatOpenAI(
        temperature=0.6,
        api_key=st.secrets["OPENAI_API_KEY"]
    )

    message = f"""
You are an activity recommendation assistant.

Weather:
{weather}

Available time: {time_available}
Preference: {preference}

Suggest:
- 3 to 5 activities
- Things to carry
- Best time (if outdoor)

Use bullet points only.
"""

    response = llm.invoke(message)
    return response.content
