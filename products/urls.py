from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    # ex. /products/
    path('products/', views.IndexView.as_view(), name='index'),
    # ex. products/2
    path('products/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex. products/2/comments
    path('products/<int:pk>/comments/', views.CommentsView.as_view(), name='comments'),
    # ex. products/2/comment
    path('products/<int:product_id>/comment/', views.comment, name='comment'),
    # ex. api/v1/products/
    path('api/v1/products/', views.IndexJsonView.as_view(), name='api_v1_index'),
    # ex. api/v1/products/2
    path('api/v1/products/<int:pk>/', views.DetailJsonView.as_view(), name='api_v1_detail'),
    # ex. api/v1/products/create_product
    path('api/v1/products/create_product', views.CreateProductJsonView.as_view(), name='api_v1_create_product'),
]
