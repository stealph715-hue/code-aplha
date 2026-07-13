from django import template

register = template.Library()


@register.filter
def is_liked_by(post, user):
    return post.is_liked_by(user)
