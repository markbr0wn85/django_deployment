from django.urls import path
from . import views

app_name = 'appfive'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('base/', views.base, name='base'),
]
