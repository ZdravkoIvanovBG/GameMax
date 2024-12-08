from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView

from GameMax.home.utils import contact_form_message
from GameMax.shop.models import Cart
from GameMax.shop.serializers import CartSerializer


class HomePage(TemplateView):
    template_name = 'home/home_page.html'


class AboutUsPage(TemplateView):
    template_name = 'home/about-us.html'


class ContactUsPage(TemplateView):
    template_name = 'home/contact.html'


def submit_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        last_name = request.POST.get('surname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        result = contact_form_message(name, last_name, email, subject, message)

        if result.status_code == 200:
            return redirect('/contact-us?success=true')
        else:
            return redirect('/contact-us?success=false')

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method.'
    })
