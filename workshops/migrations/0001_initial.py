# Generated by Django 3.2.4 on 2021-06-26 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import timezone_field.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(help_text='Name of the tag.', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Title of the workshop.', max_length=200)),
                ('start_datetime', models.DateTimeField(help_text='When this workshop will take place.')),
                ('duration', models.DurationField(help_text='How long the workshop will be.')),
                ('url', models.URLField(blank=True, help_text='Link to the workshop.')),
                ('cover_photo', models.ImageField(help_text='The cover photo of the workshop.', max_length=200, upload_to='workshop_cover_photos')),
                ('description', models.TextField(help_text='Description of the workshop.')),
                ('ingredients', models.TextField(help_text='Ingredients needed for the workshop.')),
                ('equipment', models.TextField(help_text='Equipment needed for the workshop.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the workshop is created.')),
                ('country', django_countries.fields.CountryField(help_text='The country you live in.', max_length=2)),
                ('timezone', timezone_field.fields.TimeZoneField(default='Asia/Singapore', help_text='The timezone to use as reference.')),
                ('attendees', models.ManyToManyField(blank=True, related_name='registered_workshops', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(help_text='The user this workshop is created by.', on_delete=django.db.models.deletion.CASCADE, related_name='created_workshops', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(help_text='The tags that the workshop is related to.', related_name='workshops', to='workshops.Tag')),
            ],
            options={
                'ordering': ('-start_datetime',),
            },
        ),
        migrations.CreateModel(
            name='WorkshopPost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier', primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Title of the post.', max_length=200)),
                ('content', models.TextField(help_text='Content of the post.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the post is created.')),
                ('author', models.ForeignKey(help_text='The user this post belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, help_text='Users who like this post.', related_name='posts_liked', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='WorkshopPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(help_text='The photo of taken by the user during the workshop.', max_length=200, upload_to='workshop_photos')),
                ('description', models.TextField(help_text='Description of the photo.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the photo is created.')),
                ('author', models.ForeignKey(help_text='The user this photo belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='workshop_photos', to=settings.AUTH_USER_MODEL)),
                ('workshop', models.ForeignKey(help_text='The workshop that this photo is for.', on_delete=django.db.models.deletion.CASCADE, related_name='workshop_photos', to='workshops.workshop')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='WorkshopComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identifier', primary_key=True, serialize=False)),
                ('content', models.TextField(help_text='Content of the comment.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='When the comment is created.')),
                ('author', models.ForeignKey(help_text='The user this comment belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, help_text='Users who like this comment.', related_name='comments_liked', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='workshops.workshoppost')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]