from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from spots.models import Post, Spot, Comment
from django.http import HttpResponse
from django.forms import ModelForm
from django import forms
from django.http import HttpResponseRedirect

# Create your views here.

class listspots(ListView):
    model=Spot


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
    class Meta:
        model = Post
        fields = ["title", "body"]


def showspot(request, spot_id):
    """
    Não consegui fazer com que o form fosse validado, a intenção era depois replicar 
    este código depois também para os comentários. Talvez seja algo de raiz que estou
    a fazer mal, não consegui chegar à resposta.
    """
    try:
        spot = Spot.objects.get(id=spot_id)
        print("found the spot")
    except Spot.DoesNotExist:
        return HttpResponse("404: Spot does not exist")

    queryset = Post.objects.filter(spotparent=spot)
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        print(form)
        if form.is_valid():
            print("yay")
            post = form.save(commit=False)
            post.spotparent = spot
            post.save()
            return HttpResponseRedirect(reverse('spot', args=[spot_id]))
        else:
            print(form.errors)
            print("nay")
    else:
        form = PostForm()

    context = {
        'object': queryset, 
        'form': form,
        'spot_id': spot_id,
        'spot_title': spot.title
    }
    return render(request, 'spots/spot_detail.html', context)


