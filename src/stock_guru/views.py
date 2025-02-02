from django.shortcuts import render

# Render home.html
def home(request):
    return render(request, "home.html")

def profile(request):
    return render(request,"profile.html")