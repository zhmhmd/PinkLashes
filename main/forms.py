from django import forms
from .models import Service, Master, Gallery, Review, TypeOfService, SignUp


class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["name", "img"]
        labels = {
            "name": "Название сервиса",
            "img": "Изображение",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "img": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class MasterModelForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = [
            "img", "name", "position", "experience", "description",
            "telegramm", "instagram", "tiktok", "whatsapp", "youtube",
            "services",
        ]
        labels = {
            "img": "Изображение",
            "name": "Имя",
            "position": "Позиция",
            "experience": "Опыт",
            "description": "Описание",
            "telegramm": "Телеграм",
            "instagram": "Инстаграм",
            "tiktok": "ТикТок",
            "whatsapp": "Ватсап",
            "youtube": "Ютуб",
            "services": "Сервисы",
        }
        widgets = {
            "img": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "position": forms.Select(attrs={"class": "form-control"}),
            "experience": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "telegramm": forms.URLInput(attrs={"class": "form-control"}),
            "instagram": forms.URLInput(attrs={"class": "form-control"}),
            "tiktok": forms.URLInput(attrs={"class": "form-control"}),
            "whatsapp": forms.URLInput(attrs={"class": "form-control"}),
            "youtube": forms.URLInput(attrs={"class": "form-control"}),
            "services": forms.CheckboxSelectMultiple(),
        }


class GalleryModelForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ["img", "name"]
        labels = {
            "img": "Изображение",
            "name": "Название",
        }
        widgets = {
            "img": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class ReviewModelForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["master", "score", "comment"]
        labels = {
            "master": "Мастер",
            "score": "Оценка",
            "comment": "Комментарий",
        }
        widgets = {
            "master": forms.Select(attrs={"class": "form-control"}),
            "score": forms.Select(attrs={"class": "form-control"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }


class TypeOfServiceModelForm(forms.ModelForm):
    class Meta:
        model = TypeOfService
        fields = ["title", "price", "master"]
        labels = {
            "title": "Заголовок",
            "price": "Цена",
            "master": "Мастера",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "master": forms.CheckboxSelectMultiple(),
        }

    
class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["name", "phone_number", "services", "master", "date", "time", "comment"]
        labels = {
            "name": "Имя",
            "phone_number": "Телефон",
            "services": "Сервисы",
            "master": "Мастер",
            "date": "Дата",
            "time": "Время",
            "comment": "Комментарий",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "services": forms.CheckboxSelectMultiple(),
            "master": forms.Select(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }