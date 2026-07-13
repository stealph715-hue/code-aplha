from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, instance, created, **kwargs):
    """Auto-create a Profile whenever a new User is registered."""
    if created:
        Profile.objects.create(user=instance)
