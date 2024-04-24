from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from spots.models import Post, Spot, Comment
from django.http import HttpResponse
from django.forms import ModelForm
from django import forms
from django.http import HttpResponseRedirect

# Create your views here.

class listspots(ListView):
    model=Spot

def showspot(request, spot_title):
    spot= Spot.objects.get(title=spot_title)
    queryset= Post.objects.filter(spotparent=spot)
    form = PostForm(spot_id=spot.id)
    context = {
        'object':queryset,
        'form': form,
        'spot_id': spot.id
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

class PostForm(forms.ModelForm):
    def __init__(self, spot_id=None, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.spot_id = spot_id

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.spot_id is not None:
            instance.spotparent_id = self.spot_id
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Post
        fields = ["title", "body"]


def createpost(request, spot_id):
    try:
        spot = Spot.objects.get(id=spot_id)
    except Spot.DoesNotExist:
        return HttpResponse("Spot does not exist")

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.spotparent = spot 
            post.save()
            previous_url = request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(previous_url)
    else:
        print(form.errors)
        form = PostForm()

    context = {
        'form': form,
        'spot_id': spot_id
    }
    return render(request, 'spots/spot_detail.html', context)