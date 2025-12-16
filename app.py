import streamlit as st
import requests
from agent import activity_agent

st.set_page_config(page_title="Weather Activity Suggester")

st.title("🌦 Weather-Based Activity Suggester")

city = st.text_input("Enter City Name")
time_available = st.selectbox(
    "Available Time",
    ["1 hour", "Half day", "Full day"]
)
preference = st.radio(
    "Preference",
    ["Indoor", "Outdoor"]
)

def get_weather(city):
    api_key = st.secrets["WEATHER_API_KEY"]
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return None

    return (
        f"Temperature: {data['main']['temp']} °C\n"
        f"Condition: {data['weather'][0]['description']}\n"
        f"Humidity: {data['main']['humidity']}%\n"
        f"Wind Speed: {data['wind']['speed']} m/s"
    )

if st.button("Suggest Activities"):
    if not city:
        st.error("Please enter a city name.")
    else:
        weather_summary = get_weather(city)

        if weather_summary is None:
            st.error("City not found or API error.")
        else:
            st.subheader("🌤 Weather Summary")
            st.text(weather_summary)

            st.subheader("✅ Recommended Activities")
            result = activity_agent(
                weather_summary,
                time_available,
                preference
            )
            st.write(result)
