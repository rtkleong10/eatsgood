from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django_countries import countries

from .models import Workshop, WorkshopPhoto

@require_http_methods(['GET'])
def index_view(request):
	context = {
		'countries': countries,
		'workshops': [workshop for workshop in Workshop.objects.all() if workshop.is_open_for_registration],
		'workshop_photos': WorkshopPhoto.objects.all(),
	}

	return render(request, 'workshops/index.html', context)
