
from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_doom, name="all_drdoom"),


]
