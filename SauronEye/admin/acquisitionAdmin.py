from django.contrib import admin
from SauronEye.models.acquisition import Acquisition

class AcquisitionAdmin(admin.ModelAdmin):
    list_filter=('Libelle',)
    fieldsets = (
        (None, {
            'fields': (
                'Libelle',
            )
        }),
    )
admin.site.register(Acquisition, AcquisitionAdmin)