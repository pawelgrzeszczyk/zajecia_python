from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from .form import ContactForm


class MessageAddView(FormView):
    form_class = ContactForm
    template_name = 'contact/message_form.html'
    success_url = '/'