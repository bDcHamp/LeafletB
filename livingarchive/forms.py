from typing import Any, Dict
from django import forms
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from allauth.account.forms import SignupForm

class LocalSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    institution = forms.CharField(max_length=100, label='Institution', required=False,
                              help_text='Optional: Your university, organization, or institution')

    def save(self, request):
        # First call the parent class's save method
        user = super().save(request)
        
        # Then add our custom fields
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        try:
            # Try to get the Contributors group
            contributors_group = Group.objects.get(name='Contributors')
            user.groups.add(contributors_group)
        except Group.DoesNotExist:
            # If the group doesn't exist, create it
            contributors_group = Group.objects.create(name='Contributors')
            user.groups.add(contributors_group)
        
        user.save()
        return user
