from django.db import models
from .competence import Competence

class Projet(models.Model):

    Libelle = models.CharField(max_length=100)
    Sujet = models.TextField(max_length=255)
    CompetenceNecessaire1 = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True, related_name='competence_necessaire_1')
    CompetenceNecessaire2 = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True, related_name='competence_necessaire_2')
    CompetenceNecessaire3 = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True, related_name='competence_necessaire_3')
    CompetenceNecessaire4 = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True, related_name='competence_necessaire_4')
    CompetenceNecessaire5 = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True, related_name='competence_necessaire_5')
    AutresCompetenceNecessaire = models.TextField(max_length=255, null=True, blank=True)
    CompetenceAcquise1 = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True, related_name='competence_acquise_1')
    CompetenceAcquise2 = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True, related_name='competence_acquise_2')
    CompetenceAcquise3 = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True, related_name='competence_acquise_3')
    CompetenceAcquise4 = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True, related_name='competence_acquise_4')
    CompetenceAcquise5 = models.ForeignKey(Competence, on_delete=models.CASCADE, null=True, blank=True, related_name='competence_acquise_5')
    AutresCompetenceAcquise = models.TextField(max_length=255, null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    fini = models.BooleanField(choices=[(True, 'Oui'), (False, 'Non')])
    
    def __str__(self):
        return self.Libelle