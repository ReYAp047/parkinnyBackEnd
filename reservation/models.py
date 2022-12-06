from django.db import models

class Reservation(models.Model):
    Email = models.CharField(max_length=512,blank=False)
    Matricule = models.CharField(max_length=512,blank=False)
    Adresse = models.CharField(max_length=2048, blank=False)
    Date = models.DateField(blank=False)
    Heur_arriver = models.CharField(default="", max_length=512, blank=False)
    Heur_deppart = models.CharField(max_length=512, blank=False)
    Nb_heur = models.IntegerField(blank=False)
    Prix = models.FloatField(blank=True)
    
    def __str__(self):
        return self.Email
