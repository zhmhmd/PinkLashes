from django import forms
from .models import SignUp

    
class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["name", "phone_number", "service", "master", "date", "time", "comment"]
        labels = {
            "name": "Имя",
            "phone_number": "Телефон",
            "service": "Сервисы",
            "master": "Мастер",
            "date": "Дата",
            "time": "Время",
            "comment": "Комментарий",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "service": forms.Select(attrs={"class": "form-control"}),
            "master": forms.Select(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }