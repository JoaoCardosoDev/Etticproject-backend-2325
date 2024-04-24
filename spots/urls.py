from django.urls import path
from spots import views
from spots.views import listspots, showpost, showspot

urlpatterns= [
    path("", listspots.as_view(), name="index"),
    path("<int:spot_id>/", views.showspot, name="spot"),
    path("<str:post_title>/<int:post_id>", views.showpost, name="post"),
    # path("createpost/<int:spot_id>", createpost, name="createpost")
]