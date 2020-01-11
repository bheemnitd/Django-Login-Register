from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):

    first_name = forms.CharField(max_length=100, help_text='Requird first name')
    last_name = forms.CharField(max_length=100, help_text='Requird last name')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2' )
        # unique_together = ('email',)
        # print(User._meta.local_fields[4])
        # print(User._meta.local_fields[4])

        User._meta.local_fields[7].__dict__['_unique'] = True
        #User._meta.local_fields[4].__dict__['_help_text'] = False


class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField(disabled=True)
    username = forms.CharField(disabled=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email']

# class ColorfulContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 'style': 'border-color: blue;',
#                 'placeholder': 'Write your name here'
#             }
#         )
#     )
#

