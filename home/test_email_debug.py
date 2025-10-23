from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
import smtplib
import ssl

def test_email_connection(request):
    response_text = []
    
    # Print all email-related settings
    response_text.append(f"Email Settings:")
    response_text.append(f"EMAIL_HOST: {settings.EMAIL_HOST}")
    response_text.append(f"EMAIL_PORT: {settings.EMAIL_PORT}")
    response_text.append(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
    response_text.append(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
    
    try:
        # Try to establish SMTP connection
        response_text.append("\nTesting SMTP Connection:")
        smtp = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        smtp.set_debuglevel(1)  # Enable debug output
        
        # Say hello to the server
        response_text.append("Sending EHLO...")
        smtp.ehlo()
        
        # Start TLS
        response_text.append("Starting TLS...")
        smtp.starttls(context=ssl.create_default_context())
        
        # Say hello again
        smtp.ehlo()
        
        # Try to login
        response_text.append("Attempting login...")
        smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        response_text.append("Login successful!")
        
        # Try to send test email
        response_text.append("\nAttempting to send test email...")
        send_mail(
            'Test Email from Django',
            'This is a test email to verify email settings are working.',
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        response_text.append("Test email sent successfully!")
        
        smtp.quit()
        
    except Exception as e:
        response_text.append(f"\nError: {str(e)}")
    
    return HttpResponse("<br>".join(response_text))