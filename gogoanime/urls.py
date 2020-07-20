from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('video/<str:raw_url>', views.watch_video, name='watch_video'),
]