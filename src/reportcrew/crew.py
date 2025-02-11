import logging
from dotenv import load_dotenv
from crewai import Crew
from reportcrew.task import Stock_bot
from reportcrew.agents import Stock_bot_agents
import requests
from reportcrew.chart import ChartData
import uuid
import os

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

def get_stock_symbol(stock_name):
    """Fetch the stock symbol from Yahoo Finance
    Args:
        stock_name (str): The name of the stock
    Returns: 
        stock_symbol (str): The stock symbol
    """
    try:
        stock_name = stock_name.replace(" ", " ")
        url = "https://query2.finance.yahoo.com/v1/finance/search"
        user_agent = "Chrome/8.0 (Windows NT 10.0; Win64; x64)"
        params = {"q": stock_name, "quotes_count": 1}
        res = requests.get(url=url, params=params, headers={"User-Agent": user_agent})
        res.raise_for_status()  
        data = res.json()
        stock_symbol = data["quotes"][0]["symbol"]
        logger.info(f"Fetched stock symbol for {stock_name}: {stock_symbol}")
        return stock_symbol
    except (requests.RequestException, IndexError) as e:
        logger.error(f"Failed to fetch stock symbol for {stock_name}: {e}")
        return None
    
def generate_analysis_reports(stock_symbol):
    """Generate stock analysis reports and the charts needed inside
    Args:
        stock_symbol (str): The stock symbol
    Returns:
        stock_report (str): The stock analysis report with financial chart
    """
    try:
        tasks = Stock_bot()
        agent = Stock_bot_agents()
        # Generate chart store it in ../static/
        chart = ChartData
        
        chart.generate_bar_chart(symbol = stock_symbol)
        chart.generate_line_chart(symbol = stock_symbol)

        # Create agents
        stock_analysis = agent.stock_analysis(stock_symbol)
        # Create tasks
        stock_analysis_task = tasks.stock_analysis(stock_analysis, stock_symbol)

        # Execute tasks
        stock_analysis_crew = Crew(
            agents=[stock_analysis],
            tasks=[stock_analysis_task],
            verbose=True,
            max_rpm=19,
        )
        result_stock_analysis = stock_analysis_crew.kickoff()

        logger.info(f"Generated analysis report for {stock_symbol}")
        return str(result_stock_analysis)
    except Exception as e:
        logger.error(f"Failed to generate analysis report for {stock_symbol}: {e}")
        return None

def generate_investment_reports(stock_symbol):
    """Generate stock investment reports
    Args:
        stock_symbol (str): The stock symbol
    Returns:
        stock_report (str): The stock investment report
        """
    try:
        tasks = Stock_bot()
        agent = Stock_bot_agents()

        # Create agents
        investment_analysis = agent.investment_analysis(stock_symbol)

        # Create tasks
        investment_analysis_task = tasks.investment_analysis(investment_analysis, stock_symbol)

        # Execute tasks
        investment_analysis_crew = Crew(
            agents=[investment_analysis],
            tasks=[investment_analysis_task],
            verbose=True,
            max_rpm=19,
        )

        result_investment_analysis = investment_analysis_crew.kickoff()

        logger.info(f"Generated investment report for {stock_symbol}")
        return str(result_investment_analysis)
    except Exception as e:
        logger.error(f"Failed to generate investment report for {stock_symbol}: {e}")
        return None
