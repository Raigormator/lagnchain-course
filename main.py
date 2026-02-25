# #deprecated

# from dotenv import load_dotenv

# load_dotenv()

# from langchain_classic import hub
# from langchain_classic.agents import AgentExecutor
# from langchain_classic.agents.react.agent import create_react_agent
# from langchain_ollama import ChatOllama
# from langchain_tavily import TavilySearch


# tools = [TavilySearch()]
# llm = ChatOllama(model="qwen3:1.7b")
# react_prompt = hub.pull("hwchase17/react")
# agent = create_react_agent( # reasoning agent
#     llm=llm,
#     tools=tools,
#     prompt=react_prompt,
# )

# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) # agent runtime - call a tool or run another LLM call
# chain = agent_executor

# def main():
#     # print("Hello from langchain-course")
#     result = chain.invoke(
#         input={
#             "input": "search for 1 job posting for an ai engineer using langchain in the bay area on linkedin and list their details"
#         }
#     )


# if __name__ == "__main__":
#     main()


# Pydantic Putput Parser

# from dotenv import load_dotenv

# load_dotenv()

# from langchain_classic import hub
# from langchain_classic.agents import AgentExecutor
# from langchain_classic.agents.react.agent import create_react_agent
# from langchain_core.output_parsers.pydantic import PydanticOutputParser
# from langchain_core.prompts import PromptTemplate
# from langchain_core.runnables import RunnableLambda
# from langchain_ollama import ChatOllama
# from langchain_tavily import TavilySearch

# from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
# from schemas import AgentResponse

# tools = [TavilySearch()]
# llm = ChatOllama(model="llama3.2:latest")
# react_prompt = hub.pull("hwchase17/react")
# output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
# react_prompt_with_format_instructions = PromptTemplate(
#     template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
#     input_variables=["input", "agent_scratchpad", "tool_names"],
# ).partial(format_instructions=output_parser.get_format_instructions())


# agent = create_react_agent(
#     llm=llm,
#     tools=tools,
#     prompt=react_prompt_with_format_instructions,
# )
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# extract_output = RunnableLambda(lambda x: x["output"])
# parse_output = RunnableLambda(lambda x: output_parser.parse(x))
# chain = agent_executor | extract_output | parse_output


# def main():
#     result = chain.invoke(
#         input={
#             "input": "search for 1 job posting for an ai engineer using langchain in the bay area on linkedin and list their details",
#         }
#     )
#     print(result)


# if __name__ == "__main__":
#     main()

# Structured Ouput

# from dotenv import load_dotenv

# load_dotenv()

# from langchain_classic import hub
# from langchain_classic.agents import AgentExecutor
# from langchain_classic.agents.react.agent import create_react_agent
# from langchain_core.prompts import PromptTemplate
# from langchain_core.runnables import RunnableLambda
# from langchain_ollama import ChatOllama
# from langchain_tavily import TavilySearch

# from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
# from schemas import AgentResponse

# tools = [TavilySearch()]
# llm = ChatOllama(model="llama3.2:latest")
# structured_llm = llm.with_structured_output(AgentResponse)
# react_prompt = hub.pull("hwchase17/react")
# react_prompt_with_format_instructions = PromptTemplate(
#     template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
#     input_variables=["input", "agent_scratchpad", "tool_names"],
# ).partial(format_instructions="")


# agent = create_react_agent(
#     llm=llm,
#     tools=tools,
#     prompt=react_prompt_with_format_instructions,
# )
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# extract_output = RunnableLambda(lambda x: x["output"])
# chain = agent_executor | extract_output | structured_llm


# def main():
#     result = chain.invoke(
#         input={
#             "input": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
#         }
#     )
#     print(result)


# if __name__ == "__main__":
#     main()

# create_agent

from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4o")


agent = create_agent(
    model=llm,
    tools=tools,
    response_format=AgentResponse,
)


def main():
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details",
                }
            ]
        }
    )
    # Access structured response from the agent
    structured = result.get("structured_response", None)
    print(structured if structured is not None else result)


if __name__ == "__main__":
    main()