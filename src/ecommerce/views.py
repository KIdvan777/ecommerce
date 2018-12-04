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

# shop view

def shop_view(request):
    object_list = App.objects.all()
    product_list = Product.objects.all()
    context={
        'object_list':object_list,
        'product_list':product_list
    }
    return render(request, "shop.html", context)

# detail view

def detail_view(request, pk=None, *args, **kwargs):
    object_list = App.objects.all()
    product_list = Product.objects.all()

    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)

# Featured
    # instance = Product.objects.get(pk=pk, featured=True)
    # instance = get_object_or_404(Product, pk=pk, featured=True)

# Exception for get() method ############################################################################################################33
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesnt't exist!")
    # except:
    #     print("hih")

# Filter method ############################################################################################################################
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

# Custom object manager query ##################################################################################################
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesnt't exist!")

    context={
        'object_list':object_list,
        'object':instance,
        'product_list':product_list
    }
    return render(request, "product-detail.html", context)


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
