from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile

# ----------------------------------------
# User Registration Form
# ----------------------------------------
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# ----------------------------------------
# Profile Edit Form
# ----------------------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write something about yourself...'}),
        }
        labels = {
            'bio': 'Biography',
            'avatar': 'Profile Picture',
        }
