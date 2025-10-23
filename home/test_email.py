from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def test_email(request):
    try:
        # Print settings to debug
        print("Email Settings:")
        print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
        print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
        print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
        print(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
        print(f"DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
        
        # Try to send test email
        send_mail(
            'Test Email',
            'This is a test email to verify email settings.',
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],  # Send to yourself
            fail_silently=False,
        )
        return HttpResponse("Test email sent successfully! Check the console for email settings.")
    except Exception as e:
        return HttpResponse(f"Error sending email: {str(e)}")