from django.db import models



class Adherent(models.Model):
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    validity = models.BooleanField(default=True)

    def __str__(self):
        return self.firstname + " " + self.surname

    class Meta:
        verbose_name = 'Adherent'


class GearCat(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie Materiel"


class Gear(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(GearCat, on_delete=models.DO_NOTHING, null=False)
    toRepair = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Materiel'


class Rent(models.Model):
    adherent = models.ForeignKey(Adherent, on_delete=models.DO_NOTHING, null=False)
    gear1 = models.ForeignKey(Gear, on_delete=models.DO_NOTHING, null=False)
    gear2 = models.ForeignKey(Gear, on_delete=models.DO_NOTHING, null=False)
    date = models.DateField(null=False, blank=False)
    startTime = models.TimeField(null=False, blank=False)
    returnTime = models.TimeField(null=False, blank=False)
    isDamaged = models.BooleanField(default=False)

