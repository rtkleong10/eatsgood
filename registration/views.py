from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import UserProfile


@require_http_methods(['POST', 'GET'])
def log_in(request):
	next_url = request.GET.get('next')

	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			login(request, user)

			return HttpResponseRedirect(next_url) if next_url != None else redirect("workshops:index")
	else:
		form = AuthenticationForm()

	return render(request, "registration/login.html", {'form': form, 'next_url': next_url})


@require_http_methods(['POST', 'GET'])
def sign_up(request):
	next_url = request.GET.get('next')

	if request.method == 'POST':
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)

			login(request, user)

			return HttpResponseRedirect(next_url) if next_url != None else redirect("workshops:index")

	else:
		form = UserCreationForm()

	return render(request, "registration/signup.html", {'form': form, 'next_url': next_url})


@require_http_methods(['GET'])
def log_out(request):
	logout(request)
	next_url = request.GET.get('next')
	return HttpResponseRedirect(next_url) if next_url != None else redirect("workshops:index")

@require_http_methods(['GET'])
def profile(request, username):
	user_profile = get_object_or_404(UserProfile, user__username=username)
	created_workshops = user_profile.user.created_workshops.all()
	registered_workshops = user_profile.user.registered_workshops.all()
	upcoming_workshops = []
	completed_workshops = []

	for workshop in registered_workshops:
		if workshop.is_past_workshop:
			completed_workshops.append(workshop)
		else:
			upcoming_workshops.append(workshop)

	workshop_photos = user_profile.user.workshop_photos.all()

	context = {
		'user_profile': user_profile,
		'created_workshops': created_workshops,
		'upcoming_workshops': upcoming_workshops,
		'completed_workshops': completed_workshops,
		'workshop_photos': workshop_photos,
	}

	print(upcoming_workshops)

	return render(request, "registration/profile.html", context)
