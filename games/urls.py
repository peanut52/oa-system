from django.conf.urls import url, include

from games import views

urlpatterns = [
    url(r'^index', views.game_views),
]
