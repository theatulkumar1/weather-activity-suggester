import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

def activity_agent(weather, time_available, preference):
    llm = ChatOpenAI(
        temperature=0.6,
        api_key=st.secrets["OPENAI_API_KEY"]
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an intelligent activity recommendation assistant."),
        ("human",
         """
Weather details:
{weather}

Available time: {time}
Preference: {preference}

Suggest:
- 3 to 5 suitable activities
- Things to carry
- Best time (if outdoor)

Use bullet points only.
""")
    ])

    chain = prompt | llm

    response = chain.invoke({
        "weather": weather,
        "time": time_available,
        "preference": preference
    })

    return response.content
