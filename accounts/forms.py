from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    tipo = forms.ChoiceField(choices=[
        ("cliente", "Cliente"),
        ("transportista", "Transportista")
    ])
    direccion = forms.CharField(max_length=255, required=False)

    def save(self, request):
        user = super().save(request)
        user.tipo = self.cleaned_data["tipo"]
        user.direccion = self.cleaned_data["direccion"]
        user.save()
        return user