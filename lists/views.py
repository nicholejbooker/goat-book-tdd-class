#Nichole Booker 3-11-2026

from django.shortcuts import render


def home_page(request):
    return render(request, "home.html")

