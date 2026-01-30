from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Master, Gallery, Review, TypeOfService, SignUp


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    readonly_fields = ("image_preview",)
    fields = ("image_preview", "img", "name")

    def image_preview(self, obj):
        if getattr(obj, "img", None) and obj.img:
            return format_html(
                '<img src="{}" style="height:60px; width:auto; border-radius:8px; object-fit:cover;" />',
                obj.img.url
            )
        return "—"


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview", "name", "position", "experience")
    list_display_links = ("id", "name")
    list_filter = ("position", "services")
    search_fields = ("name", "experience")
    ordering = ("id",)
    filter_horizontal = ("services",)
    readonly_fields = ("image_preview",)

    fieldsets = (
        ("Основное", {
            "fields": ("image_preview", "img", "name", "position", "experience", "description", "services")
        }),
        ("Соцсети", {
            "fields": ("telegramm", "instagram", "tiktok", "whatsapp", "youtube"),
        }),
    )

    def image_preview(self, obj):
        if getattr(obj, "img", None) and obj.img:
            return format_html(
                '<img src="{}" style="height:60px; width:auto; border-radius:8px; object-fit:cover;" />',
                obj.img.url
            )
        return "—"


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    ordering = ("id",)
    readonly_fields = ("image_preview",)
    fields = ("image_preview", "img", "name")

    def image_preview(self, obj):
        if getattr(obj, "img", None) and obj.img:
            return format_html(
                '<img src="{}" style="height:60px; width:auto; border-radius:8px; object-fit:cover;" />',
                obj.img.url
            )
        return "—"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "master", "score")
    list_display_links = ("id",)
    list_filter = ("score", "master")
    search_fields = ("master__name",)
    ordering = ("-id",)


@admin.register(TypeOfService)
class TypeOfServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    ordering = ("id",)
    filter_horizontal = ("master",)
    list_filter = ("master",)


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone_number", "master", "date", "time")
    list_display_links = ("id", "name")
    list_filter = ("date", "master", "services")
    search_fields = ("name", "phone_number", "master__name")
    ordering = ("-date", "-time")
    filter_horizontal = ("services",)

    fields = ("name", "phone_number", "master", "services", "date", "time", "comment")
