from dotenv import load_dotenv
from tavily import TavilyClient
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from typing import List
from pydantic import BaseModel, Field

load_dotenv()
# tavily = TavilyClient()

# @tool
# def search(query:str) -> str:
#     """
#     Tool that searches over internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search results as a string
#     """
#     print(f"Searching for: {query}")
#     # return "Tokyo weather is sunny"
#     return tavily.search(query=query)
    
class Source(BaseModel):
    """Schema for a source used by the the agent"""
    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    answer:str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

# llm = ChatOllama(model="llama3.2")
llm = ChatOllama(model="mistral")

# llm = ChatOpenAI()
# tools = [search]
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    # result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="search for 1 job posting for an ai engineer using langchain in the bay area on linkedin and list their details"
            )
        }
    )
    print(result)

    # print("Hello from lagnchain-course!")
#     information = """
#     Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman and entrepreneur known for his leadership of Tesla, SpaceX, Twitter, and xAI. Musk has been the wealthiest person in the world since 2025; as of February 2026, Forbes estimates his net worth to be around US$852 billion.

# Born into a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada; he has Canadian citizenship since his mother was born there. He received bachelor's degrees in 1997 from the University of Pennsylvania before moving to California to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. Musk also became an American citizen in 2002.

# In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence (AI) research, but later left; growing discontent with the organization's direction and their leadership in the AI boom in the 2020s led him to establish xAI, which became a subsidiary of SpaceX in 2026. In 2022, he acquired the social network Twitter, implementing significant changes, and rebranding it as X in 2023. His other businesses include the neurotechnology company Neuralink, which he co-founded in 2016, and the tunneling company the Boring Company, which he founded in 2017. In November 2025, a Tesla pay package worth $1 trillion for Musk was approved, which he is to receive over 10 years if he meets specific goals.

# Musk was the largest donor in the 2024 U.S. presidential election, where he supported Donald Trump. After Trump was inaugurated as president in early 2025, Musk served as Senior Advisor to the President and as the de facto head of the Department of Government Efficiency (DOGE). After a public feud with Trump, Musk left the Trump administration and returned to managing his companies. Musk is a supporter of global far-right figures, causes, and political parties. His political activities, views, and statements have made him a polarizing figure. Musk has been criticized for COVID-19 misinformation, promoting conspiracy theories, and affirming antisemitic, racist, and transphobic comments. His acquisition of Twitter was controversial due to a subsequent increase in hate speech and the spread of misinformation on the service, following his pledge to decrease censorship. His role in the second Trump administration attracted public backlash, particularly in response to DOGE.
#     """

#     summary_template = """
#     given the information {information} about a person I want you to create
#     1. A short summary
#     2. Two interesting facts about them
#     """

#     summary_prompt_template = PromptTemplate(
#         input_variables=["information"], template=summary_template
#     )

#     llm = ChatOllama(temperature=0, model="gemma3:270m")
#     chain = summary_prompt_template | llm
#     result = chain.invoke(input={"information": information})
#     print(result.content)


if __name__ == "__main__":
    main()
