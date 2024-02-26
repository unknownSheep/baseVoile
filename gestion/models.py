from django.db import models
from django.utils import timezone


class Adherent(models.Model):
    name = models.CharField(max_length=64, unique=True)
    adhesion = models.IntegerField()

    def __str__(self):
        return self.name + " __ Cotisation : " + str(self.adhesion)

    class Meta:
        verbose_name = 'Adherent'


class GearCat(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie Materiel"


class Gear(models.Model):
    name = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(GearCat, on_delete=models.DO_NOTHING, null=False)
    toRepair = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return self.category.name + ": " + self.name

    class Meta:
        verbose_name = 'Materiel'


class Emprunt(models.Model):
    adherent1 = models.ForeignKey(Adherent, on_delete=models.DO_NOTHING, related_name='adherent1')
    adherent2 = models.ForeignKey(Adherent, on_delete=models.DO_NOTHING, related_name='adherent2', blank=True, null=True)

    gear1 = models.ForeignKey(Gear, on_delete=models.DO_NOTHING, related_name='gear1', default=None)
    gear2 = models.ForeignKey(Gear, on_delete=models.DO_NOTHING, related_name='gear2', default=None, blank=True, null=True)

    startTime = models.DateTimeField(default=timezone.now, blank=False, null=False)
    returnTime = models.DateTimeField(default=None, blank=True, null=True)

    gear1IsDamaged = models.BooleanField(default=False)
    gear2IsDamaged = models.BooleanField(default=False)

    def __str__(self):
        return self.adherent1.name + " : " + self.gear1.name

    class Meta:
        verbose_name = 'Emprunt'
