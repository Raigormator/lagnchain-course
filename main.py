from dotenv import load_dotenv

load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch


tools = [TavilySearch()]


def main() -> None:
    print("Hello from langchain-course")


if __name__ == "__main__":
    main()
