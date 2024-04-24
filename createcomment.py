import os
import django
import click

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ettic.settings')
django.setup()

from django.contrib.auth import get_user_model
from spots.models import Post, Comment

@click.command()
@click.option('--post_title', prompt='Post Title', help='Title of the post associated with the comment')
@click.option('--body', prompt='Body', help='Body of the comment')
@click.option('--user_name', prompt='User Name', help='Name of the user creating the comment')
def create_comment(post_title, body, user_name):
    try:
        post = Post.objects.get(title=post_title)
        user = get_user_model().objects.get(username=user_name)

        comment = Comment.objects.create(
            body=body,
            user=user,
            postparent=post,
        )
        click.echo(f"Comment created successfully with ID: {comment.id}")
    except Post.DoesNotExist:
        click.echo("Post does not exist")
    except get_user_model().DoesNotExist:
        click.echo("User does not exist")
    except Exception as e:
        click.echo(f"Error occurred while creating the comment: {str(e)}")

if __name__ == '__main__':
    create_comment()
