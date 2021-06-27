from django.urls import path

from .views import index, workshop, workshop_signup, workshop_backout, workshop_upload

app_name = 'workshops'
urlpatterns = [
	path('', index, name='index'),
	path('workshops/<uuid:pk>/', workshop, name='workshop'),
	path('workshops/<uuid:pk>/signup', workshop_signup, name='workshop-signup'),
	path('workshops/<uuid:pk>/backout', workshop_backout, name='workshop-backout'),
	path('workshops/<uuid:pk>/upload', workshop_upload, name='workshop-upload'),
]
