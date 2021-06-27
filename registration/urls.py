from django.urls import path

from .views import log_in, sign_up, log_out, profile

app_name = 'registration'
urlpatterns = [
	path('login/', log_in, name='login'),
	path('signup/', sign_up, name='signup'),
	path('logout/', log_out, name='logout'),
	path('profile/<str:username>/', profile, name='profile'),
]
