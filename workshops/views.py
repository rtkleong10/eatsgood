from django.views.decorators.http import require_http_methods
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django_countries import countries

from .forms import WorkshopPhotoForm
from .models import Workshop, WorkshopPhoto

@require_http_methods(['GET'])
def index(request):
	context = {
		'countries': countries,
		'workshops': [workshop for workshop in Workshop.objects.all() if workshop.is_open_for_registration],
		'workshop_photos': WorkshopPhoto.objects.all(),
	}

	return render(request, 'workshops/index.html', context)

@require_http_methods(['GET'])
def workshop(request, pk):
	did_upload = False
	workshop = get_object_or_404(Workshop, pk=pk)

	if request.user.is_authenticated:
		did_upload = WorkshopPhoto.objects.filter(author=request.user, workshop=workshop).count() > 0

	context = {
		"workshop": get_object_or_404(Workshop, pk=pk),
		"did_upload": did_upload,
	}

	return render(request, 'workshops/workshop.html', context)

@require_http_methods(['POST'])
def workshop_signup(request, pk):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse('registration:login') + "?next=" + reverse('workshops:workshop', kwargs={'pk':pk}))

	workshop = get_object_or_404(Workshop, pk=pk)
	workshop.attendees.add(request.user)

	context = {
		"workshop": workshop
	}

	return render(request, 'workshops/workshop_signup.html', context)

@require_http_methods(['GET', 'POST'])
def workshop_backout(request, pk):
	if not request.user.is_authenticated:
		raise Http404

	workshop = get_object_or_404(Workshop, pk=pk)
	context = {
		"workshop": workshop,
	}

	if request.method == 'POST':
		workshop.attendees.remove(request.user)
		return render(request, 'workshops/workshop_backout_success.html', context)

	else:
		return render(request, 'workshops/workshop_backout_confirmation.html', context)

@require_http_methods(['GET', 'POST'])
def workshop_upload(request, pk):
	workshop = get_object_or_404(Workshop, pk=pk)

	if request.method == 'POST':
		workshop_photo = WorkshopPhoto(author=request.user, workshop=workshop)
		form = WorkshopPhotoForm(data=request.POST, files=request.FILES, instance=workshop_photo)

		if form.is_valid():
			form.save()
			return redirect('registration:profile', username=request.user.username)

	else:
		form = WorkshopPhotoForm()

	context = {
		"workshop": workshop,
		"form": form,
	}

	return render(request, 'workshops/workshop_photo_form.html', context)
