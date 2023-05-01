from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path("", views.home_view, name="home"),
    path("shop/", views.shop_view, name="shop"),
    path("shop/categories/<slug:slug>/", views.category_products, name="category_products")
]