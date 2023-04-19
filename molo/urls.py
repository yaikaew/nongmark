from django.urls import path

from . import views

urlpatterns = [
    path('molo/', views.molo_view, name='molo'),
]