from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import ContactForm

# --- Home page ---
def home_view(request):
    return render(request, 'pages/home.html')

# --- About page ---
def about_view(request):
    return render(request, 'pages/about.html')

# --- Contact page ---
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_message = form.save()

            # --- Email to admin ---
            subject = f"New Contact Form Submission: {contact_message.subject}"
            message = f"""
New message from {contact_message.name} ({contact_message.email})

Subject: {contact_message.subject}

Message:
{contact_message.message}
"""
            try:
                # --- Email to site admin ---
                email = EmailMessage(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,        # sender = you
                    [settings.DEFAULT_FROM_EMAIL],      # admin inbox
                    reply_to=[contact_message.email],   # reply goes to user
                )
                email.send(fail_silently=False)

                # --- Confirmation email to user ---
                confirm_subject = "We received your message"
                confirm_message = f"Hi {contact_message.name},\n\nThank you for contacting us. We'll get back to you soon!"
                confirm_email = EmailMessage(
                    confirm_subject,
                    confirm_message,
                    settings.DEFAULT_FROM_EMAIL,        # sender = you
                    [contact_message.email],            # to user
                )
                confirm_email.send(fail_silently=False)

            except Exception as e:
                print(f"Error sending email: {e}")

            # Redirect to home after successful submission
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

# --- Custom 404 page ---
def custom_404(request, exception):
    return render(request, '404.html', status=404)

# --- Test 404 page ---
def test_404(request):
    return render(request, '404.html', status=404)
