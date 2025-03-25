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
            Refer the below structure for the report and make sure to include all the necessary details.
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
                    <h1 class="text-4xl font-bold text-center text-blue-700 mb-6">Stock Analysis Report: <span id="company-name">Company Name</span></h1>
                    
                    <section class="mb-8">
                        <h2 class="text-2xl font-semibold text-gray-800 border-b pb-2">Basic Info</h2>
                        <p class="text-gray-700">A concise summary of the stock with key details.</p>
                        <table class="table-auto w-full mt-4 text-left border-collapse border border-gray-300">
                            <thead>
                                <tr class="bg-gray-200">
                                    <th class="border border-gray-300 px-4 py-2">Stock Name</th>
                                    <th class="border border-gray-300 px-4 py-2">Sector</th>
                                    <th class="border border-gray-300 px-4 py-2">Market Cap</th>
                                    <th class="border border-gray-300 px-4 py-2">P/E Ratio</th>
                                    <th class="border border-gray-300 px-4 py-2">EPS</th>
                                    <th class="border border-gray-300 px-4 py-2">Dividend Yield</th>
                                </tr>
                            </thead>
                            <tbody id="basic-info"></tbody>
                        </table>
                    </section>
                    <section class="mb-8" id="news-analysis" hidden>
                        <h2 class="text-2xl font-semibold text-gray-800 border-b pb-2">News Analysis</h2>
                        <table class="table-auto w-full mt-4 border-collapse border border-gray-300">
                            <thead>
                                <tr class="bg-gray-200">
                                    <th class="border border-gray-300 px-4 py-2">Date</th>
                                    <th class="border border-gray-300 px-4 py-2">Title</th>
                                    <th class="border border-gray-300 px-4 py-2">Description</th>
                                    <th class="border border-gray-300 px-4 py-2">Link</th>
                                </tr>
                            </thead>
                            <tbody id="news-data"></tbody>
                        </table>
                    </section>
                    <section class="mb-8" id="event-analysis" hidden>
                        <h2 class="text-2xl font-semibold text-gray-800 border-b pb-2">Event Analysis</h2>
                        <table class="table-auto w-full mt-4 border-collapse border border-gray-300">
                            <thead>
                                <tr class="bg-gray-200">
                                    <th class="border border-gray-300 px-4 py-2">Date</th>
                                    <th class="border border-gray-300 px-4 py-2">Event Title</th>
                                    <th class="border border-gray-300 px-4 py-2">Description</th>
                                </tr>
                            </thead>
                            <tbody id="event-data"></tbody>
                        </table>
                    </section>
                    <section class="mb-8">
                        <h2 class="text-2xl font-semibold text-gray-800 border-b pb-2">Trend Analysis</h2>
                        <table class="table-auto w-full mt-4 border-collapse border border-gray-300">
                            <thead>
                                <tr class="bg-gray-200">
                                    <th class="border border-gray-300 px-4 py-2">Indicator</th>
                                    <th class="border border-gray-300 px-4 py-2">Trend</th>
                                    <th class="border border-gray-300 px-4 py-2">Buy/Sell/Hold</th>
                                </tr>
                            </thead>
                            <tbody id="trend-data"></tbody>
                        </table>
                    </section>
                    <section class="mb-8">
                        <h2 class="text-2xl font-semibold text-gray-800 border-b pb-2">Financial Graphs</h2>
                        <img src="../../static/grouped_bar_chart.png" alt="Grouped Bar Chart" class="w-full my-4">
                        <img src="../../static/line_chart.png" alt="Line Chart" class="w-full my-4">
                    </section>
                    <section class="mb-8">
                        <h2 class="text-2xl font-semibold text-gray-800 border-b pb-2">Financial Analysis</h2>
                        <table class="table-auto w-full mt-4 border-collapse border border-gray-300">
                            <thead>
                                <tr class="bg-gray-200">
                                    <th class="border border-gray-300 px-4 py-2">Metric</th>
                                    <th class="border border-gray-300 px-4 py-2">Value</th>
                                </tr>
                            </thead>
                            <tbody id="financial-data"></tbody>
                        </table>
                    </section>
                    <section class="mb-8">
                        <h2 class="text-2xl font-semibold text-blue-700 border-b pb-2">Buy/Sell Values (Short & Long Term)</h2>
                        <div class="mt-4">
                            <p class="text-3xl font-bold text-green-600">Short Term (1-3 months): <span id="short-term">Buy/Sell - Price Range</span></p>
                            <p class="text-3xl font-bold text-red-600">Long Term (6-12 months): <span id="long-term">Buy/Sell - Price Range</span></p>
                        </div>
                    </section>
                </div>
            </div>
        </body>
        </html>
    
    Note :- You should not include any disclaimers or warnings in the report.
"""
            ),
            expected_output=dedent(
                f"""
            A detailed stock analysis of the {stock_symbol} stock.
            Use the correct Currency and Stock Symbol.
            The analysis should only include the following report:
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
                        <h1 class="text-4xl font-bold text-center text-blue-700 mb-6">Stock Analysis Report: <span id="company-name">Company Name</span></h1>

                        <section class="mb-8">
                            <h2 class="text-2xl font-semibold text-gray-800 border-b pb-2">Investment Report</h2>
                            
                            <div class="mb-6">
                                <h3 class="text-xl font-semibold text-green-600">Pros/Positives</h3>
                                <ul class="list-disc list-inside text-gray-700">
                                    <li>Highlight the key advantages and strengths of the stock.</li>
                                    <li>Format: Present in bullet points.</li>
                                    <li>Length: Maximum 200 words.</li>
                                </ul>
                            </div>
                            
                            <div class="mb-6">
                                <h3 class="text-xl font-semibold text-red-600">Cons/Negatives</h3>
                                <ul class="list-disc list-inside text-gray-700">
                                    <li>Identify the main drawbacks or risks associated with the stock.</li>
                                    <li>Format: Present in bullet points.</li>
                                    <li>Length: Maximum 200 words.</li>
                                </ul>
                            </div>
                            
                            <div class="mb-6">
                                <h3 class="text-xl font-semibold text-blue-600">Future Prospects</h3>
                                <ul class="list-disc list-inside text-gray-700">
                                    <li>Discuss potential growth opportunities and future developments.</li>
                                    <li>Format: Present in bullet points.</li>
                                    <li>Length: Maximum 200 words.</li>
                                </ul>
                            </div>
                            
                            <div class="mb-6">
                                <h3 class="text-xl font-semibold text-yellow-600">Risk Analysis</h3>
                                <ul class="list-disc list-inside text-gray-700">
                                    <li>Evaluate the risks associated with investing in the stock.</li>
                                    <li>Format: Present in bullet points.</li>
                                    <li>Length: Maximum 200 words.</li>
                                </ul>
                            </div>

                            <div class="mb-6">
                                <h3 class="text-2xl font-bold text-purple-700">Buy/Sell/Hold Recommendation</h3>
                                <p class="text-lg font-semibold">Based on current stock information:</p>
                                <p class="text-3xl font-bold text-green-600">BUY: <span id="buy-percentage">XX%</span></p>
                                <p class="text-3xl font-bold text-red-600">SELL: <span id="sell-percentage">XX%</span></p>
                                <p class="text-3xl font-bold text-yellow-500">HOLD: <span id="hold-percentage">XX%</span></p>
                            </div>
                        </section>
                    </div>
                </div>
            </body>
        </html>

        Note :- Do Not include Disclaimers and Warnings in the report.

        """
            ),
            expected_output=dedent(
                f"""
            A detailed stock analysis of the {stock_symbol} .
            Use the correct Currency and Stock Symbol.
            The analysis should only include the following report:
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
