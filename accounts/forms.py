from django import forms
from accounts.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['image_cover', 'image_profile']
