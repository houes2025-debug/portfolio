from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            send_mail(
                f'Portfolio: {subject}',
                f'De: {name} ^<{email}^>\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Message envoye avec succes !')
            return redirect('contact')
        except:
            messages.error(request, 'Erreur lors de l\'envoi. Reessayez.')

    return render(request, 'contact/contact.html')



