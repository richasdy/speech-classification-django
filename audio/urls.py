from django.urls import path

from . import views

app_name = 'audio'

urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:id>/edit/', views.edit, name='edit'),
    # path('<int:id>/update/', views.update, name='update'),
    # path('<int:id>/save/', views.save, name='save'),
    # path('<int:id>/delete/', views.delete, name='delete'),

    # path('', views.IndexView.as_view(), name='index'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/update/', views.update, name='update'),
    path('save/', views.save, name='save'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/process/', views.process, name='process'),
]