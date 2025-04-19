import json
import yfinance as yf
from crewai.tools import tool


class YFinanceTools:
    """A collection of tools for fetching financial data using the Yahoo Finance API."""
    @tool
    def get_company_info(symbol: str) -> str:
        """Use this function to get company information and overview for a given stock symbol.
        Args:
            symbol (str): The stock symbol.
        Returns:
            json: JSON containing company profile and overview.
        """
        try:
            company_info_full = yf.Ticker(symbol).info
            if company_info_full is None:
                return f"Could not fetch company info for {symbol}"

            company_info_cleaned = {
                "Name": company_info_full.get("shortName"),
                "Symbol": company_info_full.get("symbol"),
                "Current Stock Price": company_info_full.get('regularMarketPrice', company_info_full.get('currentPrice')),
                "Market Cap": company_info_full.get('marketCap'),
                "Sector": company_info_full.get("sector"),
                "Industry": company_info_full.get("industry"),
                "Address": company_info_full.get("address1"),
                "City": company_info_full.get("city"),
                "State": company_info_full.get("state"),
                "Zip": company_info_full.get("zip"),
                "Country": company_info_full.get("country"),
                "EPS": company_info_full.get("trailingEps"),
                "P/E Ratio": company_info_full.get("trailingPE"),
                "52 Week Low": company_info_full.get("fiftyTwoWeekLow"),
                "52 Week High": company_info_full.get("fiftyTwoWeekHigh"),
                "50 Day Average": company_info_full.get("fiftyDayAverage"),
                "200 Day Average": company_info_full.get("twoHundredDayAverage"),
                "Website": company_info_full.get("website"),
                "Summary": company_info_full.get("longBusinessSummary"),
                "Analyst Recommendation": company_info_full.get("recommendationKey"),
                "Number Of Analyst Opinions": company_info_full.get(
                    "numberOfAnalystOpinions"
                ),
                "Employees": company_info_full.get("fullTimeEmployees"),
                "Total Cash": company_info_full.get("totalCash"),
                "Free Cash flow": company_info_full.get("freeCashflow"),
                "Operating Cash flow": company_info_full.get("operatingCashflow"),
                "EBITDA": company_info_full.get("ebitda"),
                "Revenue Growth": company_info_full.get("revenueGrowth"),
                "Gross Margins": company_info_full.get("grossMargins"),
                "Ebitda Margins": company_info_full.get("ebitdaMargins"),
            }
            return json.dumps(company_info_cleaned, indent=2)
        except Exception as e:
            return f"Error fetching company profile for {symbol}: {e}"

    @tool
    def get_historical_stock_prices(
        symbol: str
    ) -> str:
        """Use this function to get the historical stock price for a given symbol.
        Args:
            symbol (str): 
                The stock symbol.
        Returns:
          json: The current stock price or error message.
        """
        try:
            stock = yf.Ticker(symbol)
            historical_price = stock.history(period='30d', interval='1d')
            return historical_price.to_json(orient="index")
        except Exception as e:
            return f"Error fetching historical prices for {symbol}: {e}"

    @tool
    def get_stock_fundamentals(symbol: str) -> str:
        """Use this function to get fundamental data for a given stock symbol yfinance API.
        Args:
            symbol (str): The stock symbol.
        Returns:
            json: A JSON string containing fundamental data or an error message.
        """
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            fundamentals = {
                "symbol": symbol,
                "company_name": info.get("longName", ""),
                "sector": info.get("sector", ""),
                "industry": info.get("industry", ""),
                "market_cap": info.get("marketCap", "N/A"),
                "pe_ratio": info.get("forwardPE", "N/A"),
                "pb_ratio": info.get("priceToBook", "N/A"),
                "dividend_yield": info.get("dividendYield", "N/A"),
                "eps": info.get("trailingEps", "N/A"),
                "beta": info.get("beta", "N/A"),
                "52_week_high": info.get("fiftyTwoWeekHigh", "N/A"),
                "52_week_low": info.get("fiftyTwoWeekLow", "N/A"),
            }
            return json.dumps(fundamentals, indent=2)
        except Exception as e:
            return f"Error getting fundamentals for {symbol}: {e}"

    @tool
    def get_income_statements(symbol: str) -> str:
        """Use this function to get income statements for a given stock symbol.
        Args:
            symbol (str): The stock symbol.
        Returns:
            json: JSON containing income statements or an empty dictionary.
        """
        try:
            stock = yf.Ticker(symbol)
            financials = stock.financials
            return financials.to_json(orient="index")
        except Exception as e:
            return f"Error fetching income statements for {symbol}: {e}"

    @tool
    def get_analyst_recommendations(symbol: str) -> str:
        """Use this function to get analyst recommendations for a given stock symbol.
        Args:
            symbol (str): The stock symbol.
        Returns:
            json: JSON containing analyst recommendations.
        """
        try:
            stock = yf.Ticker(symbol)
            recommendations = stock.recommendations
            return recommendations.to_json(orient="index")
        except Exception as e:
            return f"Error fetching analyst recommendations for {symbol}: {e}"

    @tool
    def get_company_news(symbol: str) -> str:
        """Use this function to get company news and press releases for a given stock symbol.
        Args:
            symbol (str): The stock symbol.
        Returns:
            List[dict]: A list of dictionaries containing news articles.
        """
        try:
            return yf.Search(symbol,news_count=4).news
        except Exception as e:
            return f"Error fetching company news for {symbol}: {e}"

    @tool
    def get_technical_indicators(symbol: str) -> str:
        """Use this function to get technical indicators for a given stock symbol.
        Args:
            symbol (str): The stock symbol.
        Returns:
            json: JSON containing technical indicators.
        """
        try:
            indicators = yf.Ticker(symbol).history(period='5d')
            return indicators.to_json(orient="index")
        except Exception as e:
            return f"Error fetching technical indicators for {symbol}: {e}"

    def tools():
        return [
            YFinanceTools().get_company_info,
            YFinanceTools().get_historical_stock_prices,
            YFinanceTools().get_stock_fundamentals,
            YFinanceTools().get_income_statements,
            YFinanceTools().get_analyst_recommendations,
            YFinanceTools().get_company_news,
            #YFinanceTools().get_technical_indicators,
        ]
