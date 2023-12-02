# from django.urls import path
# from .views import product_list, add_to_cart, view_cart
#
# urlpatterns = [
#     path('products/', product_list, name='product_list'),
#     path('add_to_cart/', add_to_cart, name='add_to_cart'),
#     path('view_cart/', view_cart, name='view_cart')
# ]
# myapp/urls.py

from django.urls import path
from .views import home, add_to_cart, view_cart, remove_from_cart, checkout, product_list
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    path('home', home, name='index'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view-cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('products/', product_list, name='product_list')
    # Add other URLs as needed
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)