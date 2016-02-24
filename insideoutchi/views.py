from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.


def detail(request, num):

	### REPLACE PATH WITH PATH ON SERVER TO FILE

    with open("/home/insideout/insideoutsite/insideoutchi/static/pdfs/poems/poem%s.pdf"%num, 'r') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename="poem1.pdf"'
        return response
    pdf.closed





def home(request):
	return render(request, 'home.html')

def artwork(request):
	return render(request, 'artwork.html')

def poetry(request):
    # with open("/home/AMDevG//mysite/poem_example.pdf", 'r') as pdf:
    #     response = HttpResponse(pdf.read(), content_type='application/pdf')
    #     response['Content-Disposition'] = 'inline;filename="poem_example.pdf"'
    #     return response
    # pdf.closed
    return render(request, 'poetry.html')


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

def success(request):

    if request.method == 'POST':
        name_text = request.POST.get('name', None)
        email_text = request.POST.get('mail', None)
        message_text = request.POST.get('message', None)

        send_mail('Email from Inside Out Website', message_text,"insideoutchi@gmail.com",
        ['dmoe@depaul.edu'], fail_silently=False)


        return render(request, 'success.html')

    else:
    	return HttpResponse("Sorry nothing enterd")


def thinktank(request):
	return render(request, 'thinktanks.html')




