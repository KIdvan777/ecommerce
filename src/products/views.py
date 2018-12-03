from django.views.generic import ListView, DetailView
from django.shortcuts import render,get_object_or_404
from django.http import Http404

from app.models import App
from .models import Product

# # Create your views here.

##### Class based View #############################################################################################################################################################

# List View

class ProductListView(ListView):
    object_list = App.objects.all()
    # queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args,**kwargs)
        print(context)
        object_list = App.objects.all()
        # queryset = Product.objects.all()
        context['object_list'] = object_list
        # context['product_list'] = queryset
        return context

    # custom query
    def get_queryset(self, *args, **kwargs):
        request =  self.request
        product_list = Product.objects.all()
        return product_list



##### Class based View #############################################################################################################################################################

# DetailView

class ProductDetailView(DetailView):
    object_list = App.objects.all()
    # queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        object_list = App.objects.all()
        # queryset = Product.objects.all()
        context['object_list'] = object_list
        # context['product_list'] = queryset
        return context

    # custom query
    # def get_object(self, *args, **kwargs):
    #     request =  self.request
    #     pk = self.kwargs.get('pk')
    #     product_list = Product.objects.get_by_id(pk)
    #     if product_list is None:
    #         raise Http404("Product doesnt't exist!")
    #     return product_list

    def get_queryset(self, *args, **kwargs):
        request =  self.request
        pk = self.kwargs.get('pk')
        product_list = Product.objects.filter(pk=pk)
        return product_list

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
    # instance = get_object_or_404(Product, pk=pk)

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
