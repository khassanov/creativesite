from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from datetime import datetime

from django.core.mail import send_mail, BadHeaderError
from services.forms import ContactForm
from services.models import Service, About_us, Contact, Contact_form

# Create your views here.

def services_view(request):
    contact_form = ContactForm(request.POST)
    obj_list = Service.objects.all()
    about_list = About_us.objects.all()
    contact_list = Contact.objects.all()
    context = {
        'obj_list' : obj_list,
        'about_list' : about_list,
        'contact_list' : contact_list,
        "contact_form": contact_form,
        "services_title": "УСЛУГИ",
        "about_title": "О НАС",
        "contact_title": "КОНТАКТЫ",
        'message': 'ФОРМА ОБРАТНОЙ СВЯЗИ'
    }
    if contact_form.is_valid():
            subject = contact_form.cleaned_data['name']
            second_name = contact_form.cleaned_data['second_name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            recipients = ['d-sigmat@mail.ru']
            try:
                send_mail(subject, message, 'd-sigmat@mail.ru', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
            post = contact_form.save()
            post.save()
            return render(request, "services/thank.html")
    else:
        contact_form = ContactForm()
    
    return render(request, "services/post_list.html", context)