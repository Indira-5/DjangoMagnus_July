from django import forms
from .models import Employee



class UserForm(forms.Form):
  user = forms.CharField(label="Enter the Username")
  email = forms.EmailField(label="Enter the Email")
  password = forms.CharField(label="Enter the password",widget=forms.PasswordInput)


class EmpForm(forms.ModelForm):

  class Meta:
    model = Employee
    fields = '__all__'
