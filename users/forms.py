from django.contrib.auth.forms import UserCreationForm

class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)