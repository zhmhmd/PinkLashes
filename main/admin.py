from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Master, Gallery, Review, TypeOfService, SignUp


def img_preview(obj, field_name="img"):
    f = getattr(obj, field_name, None)
    if f:
        return format_html(
            '<img src="{}" style="height:60px; width:auto; border-radius:8px; object-fit:cover;" />',
            f.url,
        )
    return "—"


@admin.register(TypeOfService)
class TypeOfServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    readonly_fields = ("image_preview",)
    fields = ("image_preview", "img", "name")

    def image_preview(self, obj):
        return img_preview(obj, "img")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "type")
    list_display_links = ("id", "title")
    search_fields = ("title", "type__name")
    list_filter = ("type", "masters")
    ordering = ("id",)
    filter_horizontal = ("masters",)


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview", "name", "position", "experience")
    list_display_links = ("id", "name")
    list_filter = ("position",)
    search_fields = ("name", "experience")
    ordering = ("id",)
    readonly_fields = ("image_preview",)

    fieldsets = (
        ("Основное", {
            "fields": ("image_preview", "img", "name", "position", "experience", "description", "type",)
        }),
        ("Соцсети", {
            "fields": ("telegramm", "instagram", "tiktok", "whatsapp", "youtube"),
        }),
    )

    def image_preview(self, obj):
        return img_preview(obj, "img")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview", "name",)
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    readonly_fields = ("image_preview",)
    fields = ("image_preview", "img", "name", "type",)

    def image_preview(self, obj):
        return img_preview(obj, "img")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "master", "score")
    list_display_links = ("id",)
    list_filter = ("score", "master")
    search_fields = ("master__name",)
    ordering = ("-id",)


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone_number", "master", "service", "date", "time")
    list_display_links = ("id", "name")
    list_filter = ("date", "master", "service")
    search_fields = ("name", "phone_number", "master__name", "service__title")
    ordering = ("-date", "-time")
    fields = ("name", "phone_number", "master", "service", "date", "time", "comment")
