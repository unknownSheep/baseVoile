from django.db import models


class Adherent(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    validity = models.BooleanField(default=True)


class Gear(models.Model):
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    lastUsed = models.ForeignKey(Adherent, on_delete=models.DO_NOTHING, null=True)
    lastUsedDate = models.DateField(null=True, blank=True)
    toRepair = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)


