"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.urls import path
# from .views import IndexView
from .views import ProductListView, product_list
from django.urls import path
from .views import index
from django.urls import path
from .views import product_list, add_product
from django.urls import path
from . import views


urlpatterns = [
    # path('', index, name='index'),
    # path('', product_list, name='product_list'),
    # path('add/', add_product, name='add_product'),
    path('products/', views.product_list, name='product_list'),
    # path('', views.index, name='index'),
    # path('', IndexView.as_view(), name='index')

    # path('products/', product_list, name='product_list'), # Функциональное представление
    # path('products-class/', ProductListView.as_view(), name='product_list_class'), # Классовое представление

]