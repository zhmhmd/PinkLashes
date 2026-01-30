import django_filters
from django import forms
from .models import Service, Master, Gallery, Review, TypeOfService, SignUp


class ServiceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Название")

    class Meta:
        model = Service
        fields = ("name",)


class MasterFilter(django_filters.FilterSet):
    position = django_filters.ChoiceFilter(
        choices=Master.POSITION_CHOICES,
        widget=forms.Select,
        empty_label="choose",
        label="Позиция",
    )
    services = django_filters.ModelMultipleChoiceFilter(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Сервисы",
    )
    name = django_filters.CharFilter(lookup_expr="icontains", label="Имя")

    class Meta:
        model = Master
        fields = ("position", "services", "name")


class GalleryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Название")

    class Meta:
        model = Gallery
        fields = ("name",)


class ReviewFilter(django_filters.FilterSet):
    master = django_filters.ModelChoiceFilter(
        queryset=Master.objects.all(),
        widget=forms.Select,
        empty_label="choose",
        label="Мастер",
    )
    score = django_filters.ChoiceFilter(
        choices=Review.SCORE_CHOICES,
        widget=forms.Select,
        empty_label="choose",
        label="Оценка",
    )

    class Meta:
        model = Review
        fields = ("master", "score")


class TypeOfServiceFilter(django_filters.FilterSet):
    master = django_filters.ModelMultipleChoiceFilter(
        queryset=Master.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Мастера",
    )
    title = django_filters.CharFilter(lookup_expr="icontains", label="Заголовок")
    price_min = django_filters.NumberFilter(field_name="price", lookup_expr="gte", label="Цена от")
    price_max = django_filters.NumberFilter(field_name="price", lookup_expr="lte", label="Цена до")

    class Meta:
        model = TypeOfService
        fields = ("master", "title")


class SignUpFilter(django_filters.FilterSet):
    master = django_filters.ModelChoiceFilter(
        queryset=Master.objects.all(),
        widget=forms.Select,
        empty_label="choose",
        label="Мастер",
    )
    services = django_filters.ModelMultipleChoiceFilter(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Сервисы",
    )
    date_from = django_filters.DateFilter(field_name="date", lookup_expr="gte", label="Дата от")
    date_to = django_filters.DateFilter(field_name="date", lookup_expr="lte", label="Дата до")

    class Meta:
        model = SignUp
        fields = ("master", "services")
