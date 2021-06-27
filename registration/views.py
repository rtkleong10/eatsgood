from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import UserProfile


@require_http_methods(['POST', 'GET'])
def log_in(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			login(request, user)
			next_url = request.GET.get('next')

			return redirect(next_url) if next_url != None else redirect("workshops:index")
	else:
		form = AuthenticationForm()

	return render(request, "registration/login.html", {'form': form})


@require_http_methods(['POST', 'GET'])
def sign_up(request):
	if request.method == 'POST':
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)

			login(request, user)
			return redirect("workshops:index")

	else:
		form = UserCreationForm()

	return render(request, "registration/signup.html", {'form': form})


@require_http_methods(['GET'])
def log_out(request):
	logout(request)
	return redirect("workshops:index")

@require_http_methods(['GET'])
def profile(request, username):
	print(get_object_or_404(UserProfile, user__username=username))
	return render(request, "registration/profile.html", {})