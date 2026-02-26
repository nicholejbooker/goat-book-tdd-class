#Nichole Booker 2-26-2026

from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<html><title>To-Do lists</title></html>")
