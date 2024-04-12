from django.db import models
from .acquisition import Acquisition

class Competence(models.Model):
    class Meta:
        verbose_name = 'Compétence'

    Libelle = models.CharField(max_length=100)
    Acqui = models.BooleanField(choices=[(True, 'Oui'), (False, 'Non')])
    NiveauAcquisition= models.ForeignKey(Acquisition, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Libelle
