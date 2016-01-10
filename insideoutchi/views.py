from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def pdf(request):
	

	### REPLACE PATH WITH PATH ON SERVER TO FILE
    with open("/Users/jberry12/Desktop/mysite/test.pdf", 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename="test.pdf"'
        return response
    pdf.closed


def home(request):
	return render(request, 'home.html')

def artwork(request):
	return render(request, 'artwork.html')

def poetry(request):
	with open("/Users/jberry12/Desktop/mysite/poem_example.pdf", 'r') as pdf:
    		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline;filename="poem_example.pdf"'
        return response
    	pdf.closed

def about(request):
	return render(request, 'about.html')


def essays(request):
	return render(request, 'essays.html')

def pdf2(request):
	with open("/Users/jberry12/Desktop/mysite/Essay1.pdf", 'r') as pdf:
        	response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename="Essay1.pdf"'
        return response
    	pdf.closed

def test(request):
	return render(request, 'test.html')

def one(request):
	return render(request, 'one.html')


def two(request):
	return render(request, 'two.html')

def three(request):
	return render(request, 'three.html')

def contact(request):
	return render(request, 'contact.html')




