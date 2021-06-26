import uuid
import datetime
from django.utils import timezone
from django.conf import settings
from django.db import models
from timezone_field import TimeZoneField
from django_countries.fields import CountryField
import pytz


class Tag(models.Model):
	name = models.SlugField(
		help_text='Name of the tag.',
		max_length=200,
		unique=True,
	)

	def __str__(self):
		return self.name


class Workshop(models.Model):
	id = models.UUIDField(
		help_text='Unique identifier',
		primary_key=True,
		default=uuid.uuid4,
		editable=False,
	)

	author = models.ForeignKey(
		help_text='The user this workshop is created by.',
		to=settings.AUTH_USER_MODEL,
		related_name='created_workshops',
		on_delete=models.CASCADE,
	)

	title = models.CharField(
		help_text='Title of the workshop.',
		max_length=200,
	)

	start_datetime = models.DateTimeField(
		help_text='When this workshop will take place.',
	)

	duration = models.DurationField(
		help_text='How long the workshop will be.',
	)

	url = models.URLField(
		help_text='Link to the workshop.',
		blank=True,
	)

	tags = models.ManyToManyField(
		help_text='The tags that the workshop is related to.',
		to=Tag,
		related_name='workshops',
	)

	cover_photo = models.ImageField(
		help_text='The cover photo of the workshop.',
		upload_to='workshop_cover_photos',
		max_length=200,
	)

	description = models.TextField(
		help_text='Description of the workshop.',
	)

	ingredients = models.TextField(
		help_text='Ingredients needed for the workshop.',
	)

	equipment = models.TextField(
		help_text='Equipment needed for the workshop.',
	)

	created_at = models.DateTimeField(
		help_text='When the workshop is created.',
		auto_now_add=True,
	)

	attendees = models.ManyToManyField(
		to=settings.AUTH_USER_MODEL,
		related_name='registered_workshops',
		blank=True,
	)

	country = CountryField(
		help_text='The country you live in.',
	)

	timezone = TimeZoneField(
		help_text='The timezone to use as reference.',
		default='Asia/Singapore',
	)

	@property
	def is_open_for_registration(self):
		return (self.start_datetime + datetime.timedelta(hours=24)) >= timezone.now()

	@property
	def is_past_workshop(self):
		return timezone.now() >= self.start_datetime

	@property
	def formatted_start_datetime(self):
		return self.start_datetime.astimezone(tz=self.timezone).strftime("%a, %b %-d · %-I:%M %p %Z")

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-start_datetime',)


class WorkshopPhoto(models.Model):
	workshop = models.ForeignKey(
		help_text='The workshop that this photo is for.',
		to=Workshop,
		on_delete=models.CASCADE,
		related_name='workshop_photos',
	)

	author = models.ForeignKey(
		help_text='The user this photo belongs to.',
		to=settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='workshop_photos',
	)
	
	photo = models.ImageField(
		help_text='The photo of taken by the user during the workshop.',
		upload_to='workshop_photos',
		max_length=200,
	)

	description = models.TextField(
		help_text='Description of the photo.',
	)

	created_at = models.DateTimeField(
		help_text='When the photo is created.',
		auto_now_add=True,
	)

	def __str__(self):
		return self.description

	class Meta:
		ordering = ('-created_at',)


class WorkshopPost(models.Model):
	id = models.UUIDField(
		help_text='Unique identifier',
		primary_key=True,
		default=uuid.uuid4,
		editable=False,
	)

	author = models.ForeignKey(
		help_text='The user this post belongs to.',
		to=settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='posts',
	)

	title = models.CharField(
		help_text='Title of the post.',
		max_length=200,
	)

	content = models.TextField(
		help_text='Content of the post.',
	)

	likes = models.ManyToManyField(
		help_text='Users who like this post.',
		to=settings.AUTH_USER_MODEL,
		related_name='posts_liked',
		blank=True,
	)

	created_at = models.DateTimeField(
		help_text='When the post is created.',
		auto_now_add=True,
	)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('created_at',)


class WorkshopComment(models.Model):
	id = models.UUIDField(
		help_text='Unique identifier',
		primary_key=True,
		default=uuid.uuid4,
		editable=False,
	)

	author = models.ForeignKey(
		help_text='The user this comment belongs to.',
		to=settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='comments',
	)

	post = models.ForeignKey(
		WorkshopPost,
		on_delete=models.CASCADE,
		related_name='comments',
	)

	content = models.TextField(
		help_text='Content of the comment.',
	)

	likes = models.ManyToManyField(
		help_text='Users who like this comment.',
		to=settings.AUTH_USER_MODEL,
		related_name='comments_liked',
		blank=True,
	)

	created_at = models.DateTimeField(
		help_text='When the comment is created.',
		auto_now_add=True,
	)

	def __str__(self):
		return self.content

	class Meta:
		ordering = ('-created_at',)
