import streamlit as st
from agent import agent

st.set_page_config(page_title="Weather Activity Suggester", page_icon="🌦️")

st.title("🌦️ Weather-Based Activity Suggester")
st.write("AI-powered activity recommendations using LangChain Agent")

city = st.text_input("Enter city name")

if st.button("Get Suggestion"):
    if city:
        with st.spinner("Analyzing weather..."):
            prompt = f"""
            You are a smart activity recommendation system.
            Get the weather for {city} and suggest 2–3 suitable activities.
            """
            result = agent.run(prompt)
            st.success("Suggested Activities:")
            st.write(result)
    else:
        st.warning("Please enter a city name.")
