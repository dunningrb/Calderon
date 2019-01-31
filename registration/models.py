from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='')


class Connection(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='current_user', null=True, on_delete=models.CASCADE)

    @classmethod
    def add_connection(cls, current_user, new_friend):
        connection, created = cls.objects.get_or_create(current_user=current_user)
        connection.users.add(new_friend)

    @classmethod
    def remove_connection(cls, current_user, removed_friend):
        # connection, created = cls.objects.get_or_created(current_user=current_user)
        connection = cls.objects.get(current_user=current_user)
        connection.users.remove(removed_friend)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
