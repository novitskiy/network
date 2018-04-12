from django import forms
from .models import *


class SubscriberForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'type': 'email',
                   'placeholder': 'Введите Ваш email ...'
            }
        )
    )

