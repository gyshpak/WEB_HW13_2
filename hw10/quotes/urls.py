from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),  # quotes:root
    path("<int:page>", views.main, name="root_paginate"),
    path("author/<str:authors>", views.author, name="author"),
    path("tag/<str:tag>", views.tag, name="tag"),
    path("add_new_author", views.add_author, name="add_author"),
    path("add_new_quote", views.add_quote, name="add_quote"),
]
