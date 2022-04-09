from django.forms import ModelForm
from Login.models import User, Profile


from django.contrib.auth.forms import UserCreationForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('__all__')
        exclude = ('user',)


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password',)
        #fields = ('email', 'password_1', 'password_2',)
