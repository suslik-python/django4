from django.urls import path
from .views import main_page, create_products

urlpatterns = [
    path('', main_page, name="main_page"),
    path('create-product/', create_products, name="create_product")
]