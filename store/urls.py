from django.urls import path
from .views import *
app_name = 'store'
urlpatterns = [
    path('',store , name='store'),
    path('<slug:category_slug>/',store , name='products_by_category'),
    path('store/<slug:product_slug>/',product_details , name='products_details'),
]

