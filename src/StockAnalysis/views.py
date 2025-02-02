from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import StockAnalysis
from reportcrew.crew import get_stock_symbol, generate_analysis_reports

@login_required
def analyze_stock(request):
    if request.method == "POST":
        stock_name = request.POST.get("stock_name")
        error_message = None
        
        if not stock_name:
            error_message = "Stock name is required"
        
        if not error_message:
            stock_symbol = get_stock_symbol(stock_name)
            if not stock_symbol:
                error_message = "Stock symbol not found"
        
        if not error_message:
            analysis_report = generate_analysis_reports(stock_symbol)
            
            StockAnalysis.objects.create(
                user=request.user, stock_name=stock_name, stock_symbol=stock_symbol, analysis_report=analysis_report
            )
            return render(request, "report/analyze_stock.html", {"analysis_report": analysis_report})

        # If there's an error message, render the template with the message
        return render(request, "report/analyze_stock.html", {"error_message": error_message})

    return render(request, "report/analyze_stock.html")
