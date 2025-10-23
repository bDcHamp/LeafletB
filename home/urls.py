from django.urls import path
from . import views
from . import test_email
from . import test_email_debug

urlpatterns = [
    path("", views.index, name="index"),
    path("test-email/", test_email.test_email, name="test_email"),
    path("test-email-debug/", test_email_debug.test_email_connection, name="test_email_debug"),
]
