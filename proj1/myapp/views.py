from django.shortcuts import render
from django.http import HttpResponse
from django. template import loader
from .models import User, Product

# Create your views here.
def myapp(request):
    myusers= User.objects.all().values()
    myproducts = Product.objects.all().values()
    template =loader.get_template('index.html')
    context ={
        'userlist' : myusers,
        'productlist':myproducts
    }
    return HttpResponse(template.render(context,request))

def prod_details(request, id):
    product = Product.objects.get(id = id)
    context = {
        'product': product
        }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context, request))

def user_details(request, pk):
    user = User.objects.get(User_id = pk)
    context ={
        'user': user
    }
    template = loader.get_template('user_details.html')
    return HttpResponse(template.render(context, request))


def userLogin(request):
    return HttpResponse("Hi, the login page is yet to be built !!!")


