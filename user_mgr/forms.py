from django import forms
from django.contrib.auth.models import User
from user_mgr.models import UserAccount

class UserRegistrationForm(forms.ModelForm):
    first_name      = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name', 'required':'required'}))
    last_name       = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name', 'required':'required'}))
    username        = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username', 'required':'required'}))
    email           = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address', 'required':'required'}))
    password        = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'required':'required'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')



class UserLoginForm(forms.ModelForm):
    email           = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Address', 'required':'required'}))
    password        = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password', 'required':'required'}))

    class Meta:
        model = User
        fields = ('email', 'password')

class UserAccountForm(forms.ModelForm):
    phone_number            = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number', 'required':'required'}))
    gender                  = forms.CharField(max_length=1, widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Gender', 'require':'required'}))
    status                  = forms.CharField(max_length=100, widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Status', 'require':'required'}))
    occupation              = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ocupation', 'require':'required'}))

    class Meta:
        model = UserAccount
        fields = ('phone_number', 'gender', 'status', 'occupation')
