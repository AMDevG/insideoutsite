from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pdf(request):
	

	### REPLACE PATH WITH PATH ON SERVER TO FILE
    with open("/Users/jberry12/Desktop/test.pdf", 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename="test.pdf"'
        return response
    pdf.closed


def home(request):
	return render(request, 'home.html')

def artwork(request):
	return render(request, 'artwork.html')



def poetry(request):
	return render(request, 'poetry.html')



def essays(request):
	return render(request, 'essays.html')

def test(request):
	return render(request, 'test.html')

def one(request):
	return render(request, 'one.html')


def two(request):
	return render(request, 'two.html')

def three(request):
	return render(request, 'three.html')



