from django.views.generic.edit import CreateView
from .models import Link

class LinkCreate(CreateView):
	model = Link
	fields = ["url"]
