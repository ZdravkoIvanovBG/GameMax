from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from mailjet_rest import Client

from GameMax import settings
from GameMax.home.utils import contact_form_message
from GameMax.shop.models import Franchise


class HomePage(ListView):
    model = Franchise
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

        success = 'true' if result.status_code == 200 else 'false'

        return redirect(f'/contact-us?success={success}')

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method.'
    })


def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')

        print(email)

        mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY), version='v3.1')

        data = {
            'Messages': [
                {
                    "From": {
                        "Email": "zdravkobg1321@students.softuni.bg",
                        "Name": "GAMEMAX"
                    },
                    "To": [
                        {
                            "Email": email,
                            "Name": "Subscriber"
                        }
                    ],
                    "Subject": "Welcome to GAMEMAX Newsletter!",
                    "TextPart": "Thank you for subscribing to the GAMEMAX newsletter. Stay tuned for updates!",
                    "HTMLPart": "<h3>Thank you for subscribing to the GAMEMAX newsletter!</h3><p>Stay tuned for "
                                "updates.</p>",
                }
            ]
        }

        result = mailjet.send.create(data=data)

        print(result.status_code)

        if result.status_code == 200:
            return redirect('home')
        else:
            return redirect('contact-us')

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method.'
    })
