from django import forms
from .models import Product
from django.contrib.auth.models import User
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','file']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm',widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=['username','email','first_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']


