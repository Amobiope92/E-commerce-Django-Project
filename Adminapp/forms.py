from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import product


class UserRegForm(UserCreationForm):

    def __init__(self,*args,**kwargs):
        super(UserRegForm,self).__init__(*args, **kwargs)
        self.fields["username"].label = "Your username"
        self.fields["username"].widget=forms.TextInput(attrs={"class":"form-control"})
        self.fields["first_name"].widget=forms.TextInput(attrs={"class":"form-control"})
        self.fields["last_name"].widget=forms.TextInput(attrs={"class":"form-control"})
        self.fields["email"].widget=forms.TextInput(attrs={"class":"form-control"})
        self.fields["password1"].widget=forms.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].label = "confirm password"
        self.fields["password2"].widget=forms.PasswordInput(attrs={"class":"form-control"})

    class Meta:
        model = User
        # fields = "__all__"
        fields = ["username","first_name","last_name", "email", "password1", "password2"] 






# class signupforms(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control'}))
#     confirm_password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control'}))

class log_in(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control'}))

class change_password(PasswordChangeForm):
    # def __init__(self,*args,**kwargs):
    #     super(change_password,self).__init__(*args, **kwargs)
    #     # self.fields["username"].label = "Your username"
    #     self.fields["old_password"].widget=forms.TextInput(attrs={"class":"form-control"})
    #     self.fields["new_password1"].widget=forms.TextInput(attrs={"class":"form-control"})
    #     self.fields["new_password2"].widget=forms.TextInput(attrs={"class":"form-control"})
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
   

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ['product_id','date','category','quantity','price','description']

        widgets = {
            'description':forms.Textarea(attrs={'cols':100, 'rows':10})
        }

