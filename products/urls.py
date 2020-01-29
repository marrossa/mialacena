from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    # ex. /products/
    path('', views.IndexView.as_view(), name='index'),
    # ex. /all_json
    path('index_json/', views.IndexJsonView.as_view(), name='index_json'),
    # ex. /products/2
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex. /products/2/comments
    path('<int:pk>/comments/', views.CommentsView.as_view(), name='comments'),
    # ex. /products/2/comment
    path('<int:product_id>/comment/', views.comment, name='comment'),
]
