from django import forms
from api.models import MyUser,Posts,Comments
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):

    class Meta:
        model=MyUser
        fields=["first_name","last_name","username","email","phone","profile_pic","password1","password2"]


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control border border-info"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border border-info","placeholder":"enter password"}))




class PostForm(forms.ModelForm):

    class Meta:
        model=Posts
        fields=[
            "image",
            "caption"
        ]
        
        widgets={
            "image":forms.FileInput(attrs={"class":"form-control" }),
            "caption":forms.Textarea(attrs={"class":"form-control","rows":2}),
        }


class CommentForm(forms.Form):
    comment=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","rows":2}))


