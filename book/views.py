from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render
from django.views.generic import DetailView

from book.models import Book


# Create your views here.

def playground(request):
    try:
        message = EmailMessage('testing mail', 'this email is sent from django', '', ['helloadewunmi@gmail.com'])
        message.attach()
        message.send()
    except BadHeaderError:
        return HttpResponse('email_sent')
    # send_mail('testing mail', 'this email is sent from django', '', ['helloadewunmi@gmail.com'])
    # return HttpResponse('email_sent')


