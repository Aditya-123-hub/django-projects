from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name='index'),
    path('product/<int:id>/',views.detail,name='detail'),
    path('instamojo-checkout/<int:id>/', views.instamojo_checkout, name='instamojo_checkout'),
    path('instamojo-success/', views.instamojo_success, name='instamojo_success'),
    path('createproduct/',views.create_product,name='createproduct'),
    path('editproduct/<int:id>/',views.edit_product,name='editproduct'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html'),name='login'),
    path('invalid/',views.invalid,name='invalid'),
    path('purchase/',views.my_purchases,name='purchase'),
    path('sales/',views.sales,name='sales'),


]