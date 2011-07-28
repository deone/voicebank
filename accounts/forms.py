from django import forms
from django.contrib.auth.models import User

class UserJoinForm(forms.ModelForm):
    username = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
	model = User
	fields = ('first_name', 'last_name', 'username')

    def save(self, commit=True):
        user = super(UserJoinForm, self).save(commit=False)
	user.email = self.cleaned_data["username"]
        user.set_password(self.cleaned_data["password"])
	
        if commit:
            user.save()

        return user
