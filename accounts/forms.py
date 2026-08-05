from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Profile
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=commit)

        if commit:
            user.profile.role = self.cleaned_data['role']
            user.profile.save()

        return user