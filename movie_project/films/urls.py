from django.urls import path
from .views import film_create_view, film_list_view

urlpatterns = [
    path('add/', film_create_view, name='film_add'),
    path('', film_list_view, name='film_list'),
]
