from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url
from django.contrib import admin

from .views import home_view, login_view
from products.views import (
            ProductListView,
            ProductDetailView,
            ProductFeaturedListView,
            ProductFeaturedDetailView,
            ProductDetailSlugView,
            detail_view,
            shop_view
            )

urlpatterns = [
    url(r'^$', home_view, name='home'),
    url(r'^shop-fbv/$', shop_view, name='shop'),
    url(r'^product-fbv/(?P<pk>\d+)/$', detail_view),
    url(r'^shop/$', ProductListView.as_view()),
    # url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^product/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    url(r'^featured/$', ProductFeaturedListView.as_view()),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^login/$', login_view, name='login'),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
