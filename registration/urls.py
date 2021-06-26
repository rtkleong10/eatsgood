from django.urls import path

from .views import log_in, sign_up, log_out

app_name = 'registration'
urlpatterns = [
	path('views/login', log_in, name='login'),
	path('views/signup', sign_up, name='signup'),
	path('views/logout', log_out, name='logout'),
]
