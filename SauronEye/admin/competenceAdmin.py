from django.contrib import admin

from SauronEye.models.competence import Competence

class CompetenceAdmin(admin.ModelAdmin):
    list_filter=('Libelle', 'Acqui', 'NiveauAcquisition')
    list_display=('Libelle', 'Acqui', 'NiveauAcquisition')
    fieldsets = (
        (None, {
            'fields': (
                'Libelle',
                'Acqui',
                'NiveauAcquisition'
            )
        }),
    )
admin.site.register(Competence, CompetenceAdmin)