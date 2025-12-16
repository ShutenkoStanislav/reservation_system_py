from django.contrib.auth.forms import UserCreationForm
from auth_system.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields = ('username','phone_number', 'email','first_name', 'middle_name','last_name')
