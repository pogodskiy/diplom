from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import *

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UserModel
        fields = ['name','username', 'second_name', 'email', 'password', 'customer']

class LoginForm(AuthenticationForm):
    pass

class UserDeleteForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = "__all__"

class ProductForm(forms.Form):
    class Meta:
        model = Products
        fields =

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_body', 'author', 'comments']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Название'
        self.fields['post_body'].label = 'Описание'
        self.fields['author'].label = 'Автор'
        self.fields['comments'].label = 'Комментарии'

