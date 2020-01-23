from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    # ex. /products/
    path('', views.index, name='index'),
    # ex. /products/2
    path('<int:product_id>/', views.detail, name='detail'),
    # ex. /products/2/comments
    path('<int:product_id>/comments/', views.comments, name='comments'),
    # ex. /products/2/comment
    path('<int:product_id>/comment/', views.comment, name='comment'),
]
