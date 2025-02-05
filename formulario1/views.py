from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            send_mail(
                'Nuevo mensaje de contacto',
                f'Apellido y Nombre: {contact.name}\n\nEmail: {contact.email}\n\nTeléfono: {contact.phone_number}\n\nMensaje: {contact.message}',
                settings.EMAIL_HOST_USER,
                ['frenouxjuan@gmail.com'],
                fail_silently=False,
            )
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
