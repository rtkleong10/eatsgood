from django.db import models
from django.conf import settings
from timezone_field import TimeZoneField
from django_countries.fields import CountryField

from workshops.models import Tag


class UserProfile(models.Model):
    user = models.OneToOneField(
        help_text='The user to which the profile belongs to.',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    profile_picture = models.ImageField(
        help_text='The profile picture of the user.',
        upload_to='profile_pictures',
        max_length=200,
        blank=True,
    )

    name = models.CharField(
        help_text='The name of the user.',
        max_length=200,
    )

    interests = models.ManyToManyField(
        help_text='The tags that you are interested in.',
        to=Tag,
        related_name='interested_users',
        blank=True,
    )

    country = CountryField(
        help_text='The country you live in.',
        blank=True,
    )

    timezone = TimeZoneField(
        help_text='The timezone to use as reference.',
        default='Asia/Singapore',
    )

    def __str__(self):
        return self.name
