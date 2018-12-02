from django.shortcuts import render

# Create your views here.

from app.models import App, Slider

# home view
def home_view(request):
    object = App.objects.all()
    
    slider_list = Slider.objects.all()
    # page = App.objects.filter(id=id)
    context={
        'object':object,
        'slider_list':slider_list,
        # 'page':page
    }
    return render(request, "index.html", context)


#shop view
def shop_view(request):
    object = App.objects.all()
    context={
        'object':object
    }
    return render(request, "shop.html", context)


#  detail view
def detail_view(request):
    object = App.objects.all()
    context={
        'object':object
    }
    return render(request, "detail.html", context)


#  login view
def login_view(request):
    object = App.objects.all()
    context={
        'object':object
    }
    return render(request, "login.html", context)


#  contact view
def contact_view(request):
    object = App.objects.all()
    context={
        'object':object
    }
    return render(request, "contact.html", context)

#  checkout view
def checkout_view(request):
    object = App.objects.all()
    context={
        'object':object
    }
    return render(request, "checkout.html", context)

#  cart view
def cart_view(request):
    object = App.objects.all()
    context={
        'object':object
    }
    return render(request, "cart.html", context)

#  blog view
def blog_view(request):
    object = App.objects.all()
    context={
        'object':object
    }
    return render(request, "blog.html", context)


#  blog-single  view
def blog_single_view(request):
    object = App.objects.all()
    context={
        'object':object
    }
    return render(request, "blog-single.html", context)

#  404  view
def page_404_view(request):
    object = App.objects.all()
    context={
        'object':object
    }
    return render(request, "404.html", context)
