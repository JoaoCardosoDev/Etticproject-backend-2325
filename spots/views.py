from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from spots.models import Post, Spot
from django.http import HttpResponse

# Create your views here.

class listspots(ListView):
    model=Spot

def showspot(request, spot_title):
    spot= Spot.objects.get(title=spot_title)
    queryset= Post.objects.filter(spotparent=spot)
    context = {
        'object':queryset
    }
    return render(request, "spots/spot_detail.html", context)

class showpost(DetailView):
    model=Post
    slug_field="parent"
    post_id="id"