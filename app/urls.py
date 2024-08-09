from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),

    # User
    path('user', views.user_list, name='user_list'),
    path('user/create', views.create_user, name='create_user'),
    path('user/<str:username>', views.user_detail, name='user_detail'),
    path('user/<str:username>/change-status', views.change_user_status, name='change_user_status'),

    # Client
    path('client', views.client_list, name='client_list'),
    path('client/create', views.create_client, name='create_client'),
    path('client/<int:pk>', views.client_detail, name='client_detail'),
    path('client/<int:pk>/delete', views.delete_client, name='delete_client'),

    # Product
    path('subcategory/<int:pk>/create-product', views.create_product, name='create_product'),
    path('product', views.product_list, name='product_list'),
    path('product/<int:pk>', views.product_detail, name='product_detail'),

    # Category
    path('category/<int:pk>/create-subcategory', views.create_subcategory, name='create_subcategory'),
    path('category/create', views.create_category, name='create_category'),
    path('category', views.category_list, name='category_list'),
    path('subcategory/<str:slug>', views.subcategory_detail, name='subcategory_detail'),

    # Order
    path('order/<uuid:uuid>/check/pdf', views.order_check_pdf, name='order_check_pdf'),
    path('order/<uuid:uuid>/check', views.order_check, name='order_check'),
    path('order/<uuid:uuid>/delete', views.delete_order, name='delete_order'),
    path('order/create', views.create_order, name='create_order'),
    path('order', views.order_list, name='order_list'),
]
