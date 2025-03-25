from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    return render(request, "home.html")

def profile(request):
    user = User.objects.get(username=request.user.username)
    email = user.email

    if request.method == "POST":
        api_key = request.Post.get("api_key")
        if api_key:
            user.profile.API_key = api_key
            user.profile.save()

        profile_picture = request.files.get("profile_picture")
        if profile_picture:
            user.profile.profile_picture = profile_picture
            user.profile.save()

    # Get current user details like username, email, reports generated (analysis and investment reports), and their dates.
    analysis_count = user.stockanalysis_set.count()
    last_analysis_report = user.stockanalysis_set.order_by('-created_at').first()
    last_analysis_date = last_analysis_report.created_at if last_analysis_report else None
    
    investment_count = user.stockinvestment_set.count()
    last_investment_report = user.stockinvestment_set.order_by('-created_at').first()
    last_investment_date = last_investment_report.created_at if last_investment_report else None

    # Fetch all reports for the user
    analysis_reports = user.stockanalysis_set.all().exclude(analysis_report=None).exclude(analysis_report="Agent stopped due to iteration limit or time limit.").order_by('-created_at')
    investment_reports_all = user.stockinvestment_set.all().exclude(investment_report=None).exclude(investment_report="Agent stopped due to iteration limit or time limit.").order_by('-created_at')

    data = {
        "username": user.username,
        "email": email,
        "reports_generated": analysis_count,
        "reports_generated_date": last_analysis_date,
        "investment_reports": investment_count,
        "investment_reports_date": last_investment_date,
        "analysis_report": analysis_reports,
        "investment_report": investment_reports_all,
    }
    return render(request, "profile.html", data)

def about_us(request):
    team_members = [
        {"name": "Vivek Maurya", "specialization": "MERN Stack Developer", "description": "Building dynamic web applications.", "photo": "vivek.jpg"},
        {"name": "Pravin Maurya", "specialization": "Python Developer, ML", "description": "Expert in AI & Data Science.", "photo": "pravin.jpg"},
        {"name": "Manav Gateyia", "specialization": "Android Developer", "description": "Creating user-friendly mobile apps.", "photo": "vishal.jpg"},
        {"name": "Nehal Kholipaka", "specialization": "Python Developer", "description": "Scalable solutions & ML expertise.", "photo": "nehal.jpg"},
    ]
    return render(request, 'about_us.html', {"team_members": team_members})