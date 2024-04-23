from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from spots.models import Post, Spot, Comment
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


def showpost(request, post_title, post_id):
    post = Post.objects.get(id=post_id)
    QuerySet = Comment.objects.filter(postparent=post)
    context = {
        'object': QuerySet,
        'post': post
    }
    return render(request, "spots/comments_view.html", context)

