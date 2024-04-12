from django.contrib import admin
from SauronEye.models.projet import Projet

class ProjetAdmin(admin.ModelAdmin):
    list_filter=('Libelle',)
    list_display=('Libelle', 'Sujet', 'fini')
    fieldsets = (
        (None, {
            'fields': ('Libelle', 'Sujet'),
        }),
        ('Compétence Nécesssaires', {
            'fields': (
                'CompetenceNecessaire1',
                'CompetenceNecessaire2',
                'CompetenceNecessaire3',
                'CompetenceNecessaire4',
                'CompetenceNecessaire5',
                'AutresCompetenceNecessaire',
                
            )
        }),
        ('Compétence Acquises', {
            'fields': (
                'CompetenceAcquise1',
                'CompetenceAcquise2',
                'CompetenceAcquise3',
                'CompetenceAcquise4',
                'CompetenceAcquise5',
                'AutresCompetenceAcquise',
            )
        }),
        ('Dates', {
            'fields': (
                'date_debut', 
                'date_fin',
            )
        }),
        (None, {
            'fields': (
                'fini',
            )
        })
    )
admin.site.register(Projet, ProjetAdmin)