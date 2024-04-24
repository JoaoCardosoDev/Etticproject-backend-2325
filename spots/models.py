from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

#modulo spot
class Spot(models.Model):
    id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=50)
    description=models.TextField(null=False, blank=False)

    def __str__(self):
        return f"{self.title}"

#modulo posts
class Post(models.Model):
    id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=50)
    body=models.TextField(null=False, blank=False)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    spotparent=models.ForeignKey(Spot, on_delete=models.CASCADE)
    up=models.PositiveIntegerField(default=0)
    down=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

#modulo comments
class Comment(models.Model):
    id=models.BigAutoField(primary_key=True)
    body=models.TextField(null=False, blank=False)
    user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    postparent=models.ForeignKey(Post, on_delete=models.CASCADE)
    up=models.PositiveIntegerField(default=0)
    down=models.PositiveIntegerField(default=0)
        
    def __str__(self):
        return f"{self.user}'s comment -> {self.id}"