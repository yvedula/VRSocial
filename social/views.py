from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello World")

def test(request):
	context = {'today': "latest_question_list"}
	return render(request, 'test/test.html', context)

def home(request):
	context = {'today': "latest_question_list"}
	return render(request, 'test/index.html', context)

def profile(request):
	context = {'today': "latest_question_list"}
	return render(request, 'test/profile.html', context)