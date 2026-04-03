#Nichole Booker 4-3-2026

from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(
        request,
        "home.html",
        {"new_item_text": request.POST.get("item_text", "")},
    )
