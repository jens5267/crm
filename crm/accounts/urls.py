from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('account/', views.accountSettings, name="account"),
    path('user/', views.userPage, name="user"),
    path('products/', views.products, name="products"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    # path('customer/', views.customer_list, name="customers"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
