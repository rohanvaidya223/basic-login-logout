from django import forms
from django.contrib.auth.models import User

class Registration(forms.ModelForm):
    password = forms.CharField(label='Password', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields = {'first_name','last_name','username','email'}
        
    def check_password(self):
        
        if self.cleaned_data['password']!=self.cleaned_data['password2']:
            raise forms.ValidationError('PASSWORD DO NOT MATCH!!!')
        
        return self.cleaned_data['password2']