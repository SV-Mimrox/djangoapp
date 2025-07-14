from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from myapp.models import Product



# Create your views here.

def home(request):
    product = Product(
    name="Sample Product",
    price=19.99,
    description="This is a description of the sample product.",
    in_stock=True
)
    product.save()
    print(f"Product '{product.name}' added successfully!")
    response = HttpResponse("Cookies set")
    response = render(request, 'home.html')
    response.set_cookie("myCookie","Demo",max_age=3600*3)
    return response

def get_cookie(request):
    cookie_value = request.COOKIES.get('myCookie')
    return HttpResponse(f"The cookie value is: {cookie_value}")

