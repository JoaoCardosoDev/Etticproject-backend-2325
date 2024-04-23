from django.urls import path
from spots import views
from spots.views import listspots, showpost, showspot

urlpatterns= [
    path("", listspots.as_view(), name="index"),
    path("<str:spot_title>", views.showspot, name="spot"),
    path("<str:post_title>/<int:post_id>", views.showpost, name="post")
]