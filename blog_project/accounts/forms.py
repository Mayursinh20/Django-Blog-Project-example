from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupPage(UserCreationForm):
    # form = UserCreationForm(use_required_attribute=False)
    email = forms.EmailField(max_length=100,help_text='Required valid email address')
    def __init__(self, *args, **kwargs):
            super(SignupPage,self).__init__(*args, **kwargs)

            for fieldname in ['username','password1','password2']:
                self.fields[fieldname].help_text = None


    class Meta:
        model  = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

    # def save(self, commit: True):
    #     user =  super(SignupPage,self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user