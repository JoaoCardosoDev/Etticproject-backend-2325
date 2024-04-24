import os
import django
import click

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ettic.settings')
django.setup()

from django.contrib.auth.models import User
from spots.models import Post, Spot

@click.command()
@click.option('--title', prompt='Title', help='Title of the post')
@click.option('--body', prompt='Body', help='Body of the post')
@click.option('--spot_title', prompt='Spot Title', help='Title of the spot associated with the post')
@click.option('--user_name', prompt='User Name', help='Name of the user creating the post')
def create_post(title, body, spot_title, user_name):
    try:
        spot = Spot.objects.get(title=spot_title)
        user = User.objects.get(username=user_name)
        post = Post.objects.create(title=title, body=body, spotparent_id=spot.id, user=user)
        click.echo(f"Post created successfully with ID: {post.id}")
    except Spot.DoesNotExist:
        click.echo("Spot does not exist")
    except User.DoesNotExist:
        click.echo("User does not exist")
    except Exception as e:
        click.echo(f"Error occurred while creating the post: {str(e)}")

if __name__ == '__main__':
    create_post()
