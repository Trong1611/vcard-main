from django.contrib import admin

from vcard.models import VcardInformation

# Register your models here.

@admin.register(VcardInformation)
class VcardInformationAdmin(admin.ModelAdmin):
    pass