from django.contrib.auth.models import User
from django import forms
from .models import MissingPerson, FoundPerson


class UserForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class MissingForm(forms.ModelForm):

    class Meta:
        model = MissingPerson
        fields = {'FirstName', 'SecondName', 'Sex', 'AgeBeforeMissing', 'DateOfBirth', 'HairColour', 'EyesColour',
                  'Weight', 'Height', 'MissingFrom', 'MissingDate', 'RelativeID', 'RelativeRelation', 'Details',
                  'MissingPersonImage'}


class FoundForm(forms.ModelForm):
    class Meta:
        model = FoundPerson
        fields = {'Sex', 'FoundIn', 'FoundDate', 'Location', 'Details', 'FoundPersonImage'}




