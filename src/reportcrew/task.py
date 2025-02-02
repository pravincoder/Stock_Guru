from textwrap import dedent
from crewai import Task


class Stock_bot:
    # Stock Analysis Tasks
    def stock_analysis(self, agent, stock_symbol):
        return Task(
            description=dedent(
                f"""
            As a Senior Stock Analyst at Goldman Sachs, your task is to produce a comprehensive and
            professional report analyzing the stock performance of {stock_symbol}.
            Report Structure :-

            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Stock Analysis Report</title>
                <!-- Tailwind CSS -->
                <script src="https://cdn.tailwindcss.com"></script>
                <!-- Flowbite CSS -->
                <link href="https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.css" rel="stylesheet" />
            </head>
            <body class="bg-gray-100">

            <!-- Main Container -->
            <div class="container mx-auto px-6 py-12">
                <div class="bg-white shadow-lg rounded-xl p-8 mb-8">
            <h1 class = (use accordingly  we have tailwind css)>Stock Analysis Report: Company Name</h1>
            <h2 class = (use accordingly  we have tailwind css)>Basic Info</h2>
              -Length:
                -Maximum 100 words in concise paragraphs.
                -Data Presentation:
                    -Provide a table with the following details: Stock Name, Sector, Market Cap (in Crores), P/E Ratio, EPS, Dividend Yield, and Average Volume (in Thousands).
                    -Format:
                        -Average Volume should be displayed in Thousands.
            <h2 class = (>News Analysis</h2>(if present)
                -Summarize the latest news related to the stock.
                -Table Format:
                    -Include Date, News Title, Brief Description, and an optional article link
                    -Length:
                        -Maximum 200 wordss
            (if present) <h2 class = (use accordingly  we have tailwind css)>Event Analysis</h2>
                    -Content: Analyze upcoming or significant past events related to the stock.
                        -Table Format:
                            -Include Date, Event Title, and Description (e.g., dividends, earnings reports).
            <h2 >Trend Analysis</h2>
                --Time Frame: Focus on the past 1 months.
                -Content: Analyze trends using key indicators like SMA, EMA, RSI, and MACD.
                -Table Format:
                    -Include indicators with corresponding trends and suggest Buy/Sell/Hold signals.
                    -Add the Current Price, 52-Week High/Low, Volume, and Average Volume of the stock.
            <h2>Financial Graphs</h2>
                - Include the following graphs:
                    <img src="../../static/grouped_bar_chart.png" alt="Grouped Bar Chart">
                    <img src="../../static/line_chart.png" alt="Line Chart">
            <h2 >Financial Analysis</h2>
               -Content:
                -Provide an in-depth analysis of the stock's financials based on data from the Financial Agent.
                -Table Format:
                    -Highlight critical insights derived from the financial metrics.
            <h2 >Buy/Sell Values (Short and Long Term)</h2>
                 -Format:(Highligted in different colors and big font size)
                    Short term(1-3 months) , Buy or Sell , with the price range.
                    Long term(6-12 months), Buy or Sell, with the price range.
        You should not include any disclaimers or warnings in the report.
        You will be paid a large bonus if your complete report is accurate and well-structured.

                    """
            ),
            expected_output=dedent(
                f"""
            A detailed stock analysis of the {stock_symbol} stock.
            The analysis should include the following:
            <h1>Stock Analysis Report: Company Name</h1>
            <h2>Basic Info</h2>
            <h2>News Analysis</h2>
            <h2>Trend Analysis</h2>
            <h2>Financial Graphs</h2>
            <h2>Financial Analysis</h2>
            <h2>Buy/Sell Values (Short and Long Term)</h2>
            Final answer should be in HTML Format Report.
        """
            ),
            verbose=True,
            agent=agent,
        )

    # Investment Analysis Tasks
    def investment_analysis(self, agent, stock_symbol):
        return Task(
            description=dedent(
                f"""
            As a Senior Investment Analyst at Goldman Sachs,
            your task is to create a detailed report analyzing the investment potential
            of {stock_symbol}.

            Report Structure:
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Stock Analysis Report</title>
                <!-- Tailwind CSS -->
                <script src="https://cdn.tailwindcss.com"></script>
                <!-- Flowbite CSS -->
                <link href="https://cdn.jsdelivr.net/npm/flowbite@2.5.2/dist/flowbite.min.css" rel="stylesheet" />
            </head>
            <body class="bg-gray-100">

            <!-- Main Container -->
            <div class="container mx-auto px-6 py-12">
                <div class="bg-white shadow-lg rounded-xl p-8 mb-8">

            <h1 class = (use accordingly in every tag as we have tailwind css)>Investment Report: Company Name</h1>
            <h2 class = (use accordingly in every tag below as we have tailwind css)>Pros/Positives</h2>
                -Highlight the key advantages and strengths of the stock.
                -Format:
                    -Present in bullet points.
                    -Length:
                        -Maximum 200 words.
            <h2 class = (use accordingly in every tag as we have tailwind css)>Cons/Negatives</h2>
                - Identify the main drawbacks or risks associated with the stock.
                -Format:
                    -Present in bullet points.
                    -Length:
                        -Maximum 200 words.
            <h2 class = (use accordingly in every tag as we have tailwind css)>Future Prospects</h2>
               -Discuss potential growth opportunities and future developments for the stock.
               -Format:
                    -Present in bullet points.
                    -Length:
                        -Maximum 200 words.

            <h2 class = (use accordingly in every tag as we have tailwind css)>Risk Analysis</h2>
                -Evaluate the risks associated with investing in the stock.

                -Format:
                    -Present in bullet points.
                    -Length:
                        -Maximum 200 words.
            <h2 class = (use accordingly in every tag as we have tailwind css)>Buy/Sell/Hold</h2>
                -Provide a recommendation on whether to Buy, Sell, or Hold the based on current stock info.
                -Format:(Highligted in different colors and big font size)
                    BUY : Percentage
                    SELL : Percentage
                    HOLD : Percentage
        You should not include any disclaimers or warnings in the report.


        Note :- Do Not include Disclaimers and Warnings in the report.

        """
            ),
            expected_output=dedent(
                f"""
            A detailed stock analysis of the {stock_symbol} stock must be in MarkDown Format.
            The analysis should include the following:
            <h1>Investment Report: Company Name</h1>
            <h2>Pros/Positives</h2>
            <h2>Cons/Negatives</h2>
            <h2>Future Prospects</h2>
            <h2>Risk Analysis</h2>
            <h2>Buy/Sell/Hold</h2>
            Final answer should be in HTML Format Report.
            """
            ),
            agent=agent,
            verbose=True,
        )
