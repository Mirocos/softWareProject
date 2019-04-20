from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uploadWiki/', views.savePetWiki),  #use /wx/uploadWiki/
    path('getWiki/', views.getPetWiki)
]
