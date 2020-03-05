from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    mensaje = forms.CharField()