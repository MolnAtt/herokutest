from django.db import models

class Applikacio(models.Model):
    nev= models.CharField(max_length=100)
    url= models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Applikáció'
        verbose_name_plural = 'Applikációk'
    def __str__(self):
        return f'{self.nev} ({self.url})'
