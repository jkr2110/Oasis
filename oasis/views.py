from django.shortcuts import render_to_response

# Create your views here.

def index(request):
	return render_to_response('oasis/home.html')

def about(request):
	return render_to_response('oasis/about.html')

def methodology(request):
	return render_to_response('oasis/methodology.html')

def contact(request):
	return render_to_response('oasis/contact.html')

def map(request):
	return render_to_response('oasis/map.html')

def grocery(request):
	return render_to_response('oasis/grocery.html')

def restaurant(request):
	return render_to_response('oasis/restaurant.html')

def business(request):
	return render_to_response('oasis/business.html')

def citizen(request):
	return render_to_response('oasis/citizen.html')

def indicator(request):
	return render_to_response('oasis/indicator.html')