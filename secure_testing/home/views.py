from django.shortcuts import render

# Home page view
def home(request):
    return render(request, 'home/home.html')
