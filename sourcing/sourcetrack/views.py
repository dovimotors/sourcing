from django.shortcuts import render
from django.http import HttpResponse
from .models import Interview
from django.template import RequestContext, loader

def index(request):
	latest_interview_list = Interview.objects.order_by('-int_date')[:5]
	context = {'latest_interview_list': latest_interview_list}
	return render(request, 'sourcetrack/index.html', context)
	
def detail(request, interview_id):
	return HttpResponse("You're looking at question %s." % interview_id)
	
def interview(request):
	return HttpResponse("You're entering and interview.")