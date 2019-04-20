from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('petWiki/', views.test),
    path('uploadWiki', views.savePetWiki)
]
