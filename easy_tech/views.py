from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    date = datetime.now()
    context = {
        "date":date,
    }
    return render(request, "easy_tech/home.html", context)
