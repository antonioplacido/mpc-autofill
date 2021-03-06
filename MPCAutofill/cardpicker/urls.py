from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('review', views.review, name='review'),
    path('guide', views.guide, name='guide'),
    path('credits', views.credits, name='credits'),
    path('legal', views.legal, name='legal'),
    path('csvupload', views.csvupload, name='csvupload')
]
