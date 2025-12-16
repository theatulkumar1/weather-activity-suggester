import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def activity_agent(weather_summary, time_available, preference):
    llm = ChatOpenAI(
        temperature=0.6,
        openai_api_key=st.secrets["OPENAI_API_KEY"]
    )

    prompt = PromptTemplate(
        input_variables=["weather", "time", "preference"],
        template="""
You are an intelligent activity recommendation assistant.

Weather summary:
{weather}

Available time: {time}
Preference: {preference}

Provide:
1. 3–5 suitable activities
2. Things to carry
3. Best time slots (if outdoor)

Use clear bullet points.
"""
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(
        weather=weather_summary,
        time=time_available,
        preference=preference
    )

    return response
