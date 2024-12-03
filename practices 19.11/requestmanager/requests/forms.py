from .models import Request
from django.forms import ModelForm, TextInput


class ReqestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['name','email','message','submitted_at']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Имя'
            }),
            'email': TextInput(attrs={
                'placeholder': 'Почта'
            }),
            'message': TextInput(attrs={
                'placeholder': 'СОобщение'
            })
        }
