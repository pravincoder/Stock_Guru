from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from textwrap import dedent
import os
from crewai import Agent
from reportcrew.tools import YFinanceTools
from dotenv import load_dotenv
load_dotenv()

"""
llm = ChatOpenAI(
    base_url='http://localhost:11434/v1',
    model='llama3.1:latest',
    api_key='NA'
) #(If you are using Ollama)
"""
"""
llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    api_key=os.getenv('OPENAI_API_KEY')
) #(If you are using ChatGPT) 
"""

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    # Add Your API Key from (https://console.groq.com/keys)
    api_key=os.environ['GROQ_API_KEY'],
)


class Stock_bot_agents:
    def stock_analysis(self, stock_symbol):
        """Agent for Stock Analysis"""
        return Agent(
            role="Stock Analysis",
            goal="To create a report on stock analysis.",
            tools=YFinanceTools.tools(),
            backstory=dedent(
                """
            As a stock analyst you are working for a Goldman Sachs company.
            you have been assigned to create a report of the analysis of the {stock_symbol} stock.
            You must try to keep a professional tone and should meet the given Requirements.
            You will get $1000 as a bonus if you complete the task within 3 iterations.
            """
            ),
            verbose=True,
            llm=llm,
            max_rpm=19,
            max_retry_limit=2,
            allow_delegation=True,
            max_execution_time=180,
        )

    def investment_analysis(self, stock_symbol):
        """Agent for Investment Analysis"""
        return Agent(
            role="Stock Report",
            goal="To create a report of the Investment analysis.",
            tools=YFinanceTools.tools(),
            backstory=dedent(
                """
            As a Investment analyst you are working for a Goldman Sachs company.
            you have been assigned to create a report of the Investment in the {stock_symbol} stock.
            You must try to keep a professional tone and should meet the given Requirements.

            You will get $1000 as a bonus if you complete the task within 3 iterations.                                       
            """
            ),
            verbose=True,
            llm=llm,
            max_rpm=19,
            max_retry_limit=1,
            allow_delegation=True,
            max_execution_time=180,
        )
