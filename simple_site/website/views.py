from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
	context = {
		"age" : 50
	}
	return render(req, 'website/index.html', context)

