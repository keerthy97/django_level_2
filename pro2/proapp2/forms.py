from django import forms
from proapp2.models import User

class NewUserForm(forms.ModelForm):
    #here we can add any custom validation
    class Meta:
        model = User
        fields = '__all__'
