from django.contrib import admin

from spots.models import Post, Spot, Comment

# Register your models here.
@admin.register(Spot)
class SpotAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class SpotAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class SpotAdmin(admin.ModelAdmin):
    pass