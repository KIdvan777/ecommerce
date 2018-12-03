from django.views.generic import ListView, DetailView
from django.shortcuts import render,get_object_or_404

from app.models import App
from .models import Product

# # Create your views here.

##### Class based View #############################################################################################################################################################

# List View

class ProductListView(ListView):
    object_list = App.objects.all()
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args,**kwargs)
        print(context)
        object_list = App.objects.all()
        queryset = Product.objects.all()
        context['object_list'] = object_list
        context['product_list'] = queryset
        return context



##### Class based View #############################################################################################################################################################

# DetailView

class ProductDetailView(DetailView):
    object_list = App.objects.all()
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        object_list = App.objects.all()
        queryset = Product.objects.all()
        context['object_list'] = object_list
        context['product_list'] = queryset
        return context




##### Function based View ###################################################################################################################################################################

# shop view

def shop_view(request):
    object_list = App.objects.all()
    product_list = Product.objects.all()
    context={
        'object_list':object_list,
        'product_list':product_list
    }
    return render(request, "shop.html", context)


##### Function based View ###################################################################################################################################################################

# detail view

def detail_view(request, pk=None, *args, **kwargs):
    object_list = App.objects.all()
    product_list = Product.objects.all()

    # instance = Product.objects.get(pk=pk)
    instance = get_object_or_404(Product, pk=pk)
    context={
        'object_list':object_list,
        'object':instance,
        'product_list':product_list
    }
    return render(request, "product-detail.html", context)
