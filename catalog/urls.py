from django.conf.urls import *

urlpatterns = patterns('catalog.views',
    url(r'^$', 'index', {'template_name':'catalog/index.html'}, 'catalog_home'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', {'template_name':'catalog/category.html'},
        'catalog_category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', 'show_product', {'template_name':'catalog/product.html'},
        'catalog_product'),
)