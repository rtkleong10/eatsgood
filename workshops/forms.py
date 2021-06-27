from django.forms import ModelForm

from .models import WorkshopPhoto

class WorkshopPhotoForm(ModelForm):
    class Meta:
        model = WorkshopPhoto
        fields = ['photo', 'description']