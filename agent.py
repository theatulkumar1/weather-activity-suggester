from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.agents import initialize_agent, AgentType
from tools import get_weather

llm = ChatOpenAI(temperature=0.6)

weather_tool = Tool(
    name="Weather API Tool",
    func=get_weather,
    description="Fetches current weather data for a given city"
)

agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
