from django.urls import path
from .views import (home,product_list,product_detail,
                    create_product,update_product,delete_product)

urlpatterns=[
    path('',home),
    # path('products/',product_list),
    path('products/',product_list),
    path('products/<pk>/',product_detail),
    path('products/create/',create_product),
    # path('products/createe/',product_create),
    path('products/<pk>/',product_detail),
    path('products/<pk>/update/',update_product),
    path('products/<pk>/delete/',delete_product)
]
