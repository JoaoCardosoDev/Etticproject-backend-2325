import os
import django
import click

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ettic.settings')
django.setup()
from spots.models import Spot, Post


@click.command()
def list_spots_and_posts():
    spots = Spot.objects.all()

    for spot in spots:
        click.echo(f"* {spot.title} *")
        posts = Post.objects.filter(spotparent=spot)
        if posts.exists():
            for post in posts:
                click.echo(f"    - {post.title}")
        else:
            click.echo("   - Spot sem posts")
        print("\n")

if __name__ == '__main__':
    list_spots_and_posts()
