from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="book_list"),
    path("create/", views.create, name="book_create"),
    path("update/<int:id>/", views.update, name="book_update"),
    path("delete/<int:id>/", views.delete, name="book_delete"),
]