from django import forms
# from .models import HomePage

from phonenumber_field.modelfields import PhoneNumberField


class ContactForm(forms.Form):
    """ Contact form """

    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    full_name = forms.CharField(label='Your full name', max_length=255)
    phone_number = PhoneNumberField()

    class Meta:
        # model = HomePage
        fields = ['subject', 'message', 'full_name', 'phone_number']
