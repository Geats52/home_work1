from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('clients/create/', views.create_client_view, name='create_client'),
    path('clients/', views.all_clients_view, name='all_clients'),
    path('clients/<int:client_id>/update/', views.update_client_view, name='update_client'),
    path('clients/<int:client_id>/delete/', views.delete_client_view, name='delete_client'),

    path('products/create/', views.create_product, name='create_product'),
    path('products/', views.all_products, name='all_products'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),

    path('orders/', views.orders, name='orders'),

    path('get-orders-by-client/', views.get_orders_by_client, name='get_client_orders'),
    path('all-client-orders/<int:client_id>/', views.all_client_orders, name='all_client_orders'),
    path('all-client-orders/<int:client_id>/<int:period>', views.all_client_orders, name='all_client_orders'),
    path('all-client-orders/<int:client_id>/<str:unique>', views.all_client_orders, name='all_client_orders'),
    path('all-client-orders/<int:client_id>/<int:period>/<str:unique>', views.all_client_orders, name='all_client_orders'),

    path('get-product-by-id/', views.get_products_by_id, name='get_products_by_id'),
    path('get-product-by-id/<str:success_message>', views.get_products_by_id, name='get_products_by_id'),
    path('product-update/<int:product_id>/', views.products_update, name='products_update'),

]