from django.urls import path

from space import views

urlpatterns = [
    path("add_space/", views.add_space),
    path("get_spaces/", views.get_spaces)
]
