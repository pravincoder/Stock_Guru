from django.shortcuts import render

# Render home.html
def home(request):
    return render(request, "home.html")

def profile(request):
    return render(request,"profile.html")

def about_us(request):
    team_members = [
    {"name": "Vivek Maurya", "specialization": "MERN Stack Developer", "description": "Building dynamic web applications.", "photo": "vivek.jpg"},
    {"name": "Pravin Maurya", "specialization": "Python Developer, ML", "description": "Expert in AI & Data Science.", "photo": "pravin.jpg"},
    {"name": "Manav Gateyia", "specialization": "Android Developer", "description": "Creating user-friendly mobile apps.", "photo": "vishal.jpg"},
    {"name": "Nehal Kholipaka", "specialization": "Python Developer", "description": "Scalable solutions & ML expertise.", "photo": "nehal.jpg"},
]
    return render(request, 'about_us.html', {"team_members": team_members})

    