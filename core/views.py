from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get("nombre")
    context = {
        "form": form,
    }
    return render(request, "home.html", context)


def certificaciones(request):
    return render(request, "certificaciones.html")


def contact(request):
    form =  ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = "form de contacto"
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otroemail@gmail.com"]
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
            )


       # print (nombre,email,mensaje)
    context = {
        "form" : form,
    }
    return render(request,"forms.html", context)