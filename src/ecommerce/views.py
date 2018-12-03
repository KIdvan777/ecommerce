from django.shortcuts import render

# Create your views here.

from app.models import App, Slider
from products.models import Product

# home view
def home_view(request):
    object_list = App.objects.all()
    product_list = Product.objects.all()
    slider_list = Slider.objects.all()
    context={
        'object_list':object_list,
        'slider_list':slider_list,
        'product_list':product_list
    }
    return render(request, "index.html", context)

#  login view
def login_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "login.html", context)


#  contact view
def contact_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "contact.html", context)

#  checkout view
def checkout_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "checkout.html", context)

#  cart view
def cart_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "cart.html", context)

#  blog view
def blog_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "blog.html", context)


#  blog-single  view
def blog_single_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "blog-single.html", context)

#  404  view
def page_404_view(request):
    object_list = App.objects.all()
    context={
        'object_list':object_list
    }
    return render(request, "404.html", context)
