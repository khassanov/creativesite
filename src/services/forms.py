from django import forms
from services.models import Contact_form


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_form
        fields = ('name', 'second_name', 'email', 'message')