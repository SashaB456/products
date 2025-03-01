from django.shortcuts import render, request
from django.http import HttpResponse
# Create your views here.
from customers.models import Product, Review
def post_review(request):
    if request.method == "POST":
        author = request.POST.get("user")
        text = request.POST.get("text")
        rating = request.POST.get("rating")
        try:
            product = Product.objects.get(author=author)
        except ValueError:
            HttpResponse("Not found", status=400)