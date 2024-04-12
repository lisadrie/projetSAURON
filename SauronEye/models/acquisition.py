from django.db import models

class Acquisition(models.Model):
    class Meta:
        verbose_name = 'Acquisition'

    Libelle = models.CharField(max_length=100)

    def __str__(self):
        return self.Libelle