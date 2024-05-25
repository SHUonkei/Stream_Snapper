from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next', views.next, name="next"),
    path('formpage', views.FormView.as_view(),name="formpage"),
    path('video-list', views.videoListView, name='videoListView'),
    path('GenerateUrl', views.generateUrlView.as_view(), name='GenerateUrl'),
    path('analyzeUrl', views.analyzeUrlView.as_view(), name='analyzeUrl'),
    ]
