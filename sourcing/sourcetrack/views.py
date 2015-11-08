from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Hello, world. You are at the sourcing index")
	
def detail(request, interview_id):
	return HttpResponse("You're looking at question %s." % interview_id)
	
def interview(request, interview_id):
	return HttpResponse("You're entering and interview %s." % interview_id)