from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as _UserAdmin, _


@admin.register(models.User)
class UserAdmin(_UserAdmin):
    _UserAdmin.fieldsets += (
        (
            None,
            {"fields": ("emailPass",)},
        ),
    )


@admin.register(models.Placeholder)
class PlaceholderAdmin(admin.ModelAdmin):
    list_display = ("kind", "name", "x", "y", "template", "created_at")
    list_filter = ("kind", "template")
    search_fields = ("name",)


@admin.register(models.CertificateTemplate)
class CertificateTemplateAdmin(admin.ModelAdmin):
    list_display = ("image", "user", "created_at")
    list_filter = ("user",)
    search_fields = ("user",)


@admin.register(models.CertificateSession)
class CertificateSessionAdmin(admin.ModelAdmin):
    list_display = ("user", "template", "created_at", "reciever_count")
    list_filter = ("user", "template")
    search_fields = ("user", "template")

    def reciever_count(self, obj):
        return obj.recievers.count()


@admin.register(models.reciever)
class recieverAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "extra")
    list_filter = ("name", "email")
    search_fields = ("name", "email")


@admin.register(models.recieved_certificate)
class recieved_certificateAdmin(admin.ModelAdmin):
    list_display = ("id", "reciever", "template")
    list_filter = ("reciever", "template")
    search_fields = ("reciever", "template")
