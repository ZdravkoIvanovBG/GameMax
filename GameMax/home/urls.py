from django.urls import path

from GameMax.home.views import HomePage, AboutUsPage, ContactUsPage, submit_form, subscribe_newsletter

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('about-us/', AboutUsPage.as_view(), name='about-us'),
    path('contact-us/', ContactUsPage.as_view(), name='contact-us'),
    path('submit-form/', submit_form, name='submit_form'),
    path('subscribe-newsletter/', subscribe_newsletter, name='subscribe_newsletter')
]
