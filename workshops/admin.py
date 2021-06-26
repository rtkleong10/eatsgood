from django.contrib import admin
from .models import Tag, Workshop, WorkshopPhoto, WorkshopPost, WorkshopComment

admin.site.register(Tag)
admin.site.register(Workshop)
admin.site.register(WorkshopPhoto)
admin.site.register(WorkshopPost)
admin.site.register(WorkshopComment)
