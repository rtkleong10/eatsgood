from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def log_in(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)

		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			login(request, user)
			next_url = request.GET.get('next')

			return redirect(next_url) if next_url != None else redirect("blog:index")
	else:
		form = AuthenticationForm()

	return render(request, "registration/login.html", {'form': form})


def sign_up(request):
	if request.method == 'POST':
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)

			login(request, user)
			return redirect("blog:index")

	else:
		form = UserCreationForm()

	return render(request, "registration/signup.html", {'form': form})


def log_out(request):
	logout(request)
	return redirect("blog:index")
