from django.urls import path

from . import views

app_name = 'hmpg'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
