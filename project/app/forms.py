from django import forms
from django.core import validators
from .models import *


GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female'),
]
def phone_field(phone):
	if not (phone.isdigit() and len(phone)==10):
		raise ValidationError("%(phone)s must be 10 digit")
		
class MyForm(forms.Form):

    NAME = forms.CharField(max_length=50)
    EmailId = forms.EmailField(validators=[validators.EmailValidator()])
    MOBILENUMBER = forms.IntegerField(validators=[phone_field])
    AGE = forms.IntegerField()
    GENDER = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    ADDRESS = forms.CharField(max_length=50)

class ImageForm(forms.ModelForm):
	class Meta:
		model= Image
		fields = '__all__'

class StudentForm(forms.ModelForm):
	class Meta:
		model= Student
		fields = '__all__'







   
