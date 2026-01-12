from django.urls import path
from .views import main_page, create_product

urlpatterns = [
    path('', main_page, name="main_page"),
    path('create-product/', create_product, name="create_product")
]