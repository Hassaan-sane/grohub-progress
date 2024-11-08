"""
URL configuration for progress_reporting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from emp_rprt import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path("admin/", admin.site.urls),
    path('product-progress/', views.product_progress_view, name='product_progress'), 
    path('save-progress/', views.save_progress_view, name='save_progress'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('data-entry/', views.data_entry, name='data_entry'),
    path('user-progress/', views.user_progress, name='user_progress'),
    path('view-all-products/', views.view_all_products, name='view_all_products'),
    path('product/<str:sku>/', views.product_detail, name='single_product'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
