from django.urls import path

from . import views

app_name = 'grade'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/process/', views.process, name='process'),
]