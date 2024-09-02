from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from .models import Contact
from .models import Book

from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Save to database
        contact_entry = Contact(name=name, email=email, subject=subject, message=message)
        contact_entry.save()

        # Prepare full message
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            # Send email
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['bogiannab@gmail.com'],
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except Exception as e:
            return HttpResponse(f'An error occurred: {e}')

        return redirect('thanks')

    return render(request, 'contact.html')

def quote(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        service = request.POST['service']
        message = request.POST['message']

        # Save to database
        contact_entry = Contact(name=name, email=email, service=service, message=message)
        contact_entry.save()

        # Prepare full message
        full_message = f"Name: {name}\nEmail: {email}\nService: {service}\n\nMessage:\n{message}"

        try:
            # Send email
            send_mail(
                service,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['bogiannab@gmail.com'],
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except Exception as e:
            return HttpResponse(f'An error occurred: {e}')

        return redirect('thanks')

    return render(request, 'quote.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

from django.shortcuts import render


def portfolio(request):
    books = Book.objects.all().order_by('-date_added')  # Sort by date_added in descending order
    return render(request, 'portfolio.html', {'books': books})

def thanks(request):
    return render(request, 'thanks.html')

def service(request):
    return render(request, 'service.html')

def blog(request):
    return render(request, 'blog.html')

def detail(request):
    return render(request, 'detail.html')

def feature(request):
    return render(request, 'feature.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def price(request):
    return render(request, 'price.html')

