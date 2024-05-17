from django.db import models
from django.utils import timezone


class Adherent(models.Model):
    name = models.CharField(max_length=64, unique=False, blank=False)
    firstName = models.CharField(max_length=64, unique=False, blank=False)
    adhesion = models.IntegerField(null=True, blank=True)
    entreprise = models.CharField(max_length=64, unique=False, blank=True, null=True)

    def __str__(self):
        adherentString = self.name + " " + self.firstName
        if self.entreprise is not None:
            adherentString += " " + str(self.entreprise)
        if self.adhesion is not None:
            adherentString += " __ Cotisation : " + str(self.adhesion)
        return adherentString
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.firstName = self.firstName.title()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Adherent'


class GearCat(models.Model):
    name = models.CharField(max_length=64, unique=True)
    level = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie Materiel"


class Gear(models.Model):
    name = models.CharField(max_length=64, unique=False)
    category = models.ForeignKey(GearCat, on_delete=models.DO_NOTHING, null=False)
    isInService = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    codeImo = models.CharField(max_length=64, unique=False, null=True, blank=True)

    def __str__(self):
        return self.category.name + ": " + self.name

    class Meta:
        verbose_name = 'Materiel'


class Reparation(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.DO_NOTHING, related_name='gear', default=None)
    dateDebut = models.DateTimeField(default=timezone.now, blank=False, null=False)
    dateFin = models.DateTimeField(default=None, blank=True, null=True)
    commentaire = models.CharField(max_length=256)

    def __str__(self):
        return self.commentaire + " de : " + str(self.gear)


class Emprunt(models.Model):
    adherent1 = models.ForeignKey(Adherent, on_delete=models.DO_NOTHING, related_name='adherent1')
    adherent2 = models.ForeignKey(Adherent, on_delete=models.DO_NOTHING, related_name='adherent2', blank=True,
                                  null=True)

    gear1 = models.ForeignKey(Gear, on_delete=models.DO_NOTHING, related_name='gear1', default=None)
    gear2 = models.ForeignKey(Gear, on_delete=models.DO_NOTHING, related_name='gear2', default=None, blank=True,
                              null=True)

    startTime = models.DateTimeField(default=timezone.now, blank=False, null=False)
    returnTime = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.adherent1.name + " : " + self.gear1.name

    def get_image(self):
        assert self.gear1 is not None

        if self.gear2 is None:
            if self.gear1.photo is not None:
                return self.gear1.photo.url
            else:
                return None
        else:
            if self.gear1.photo is None:
                return self.gear2.photo.url
            elif self.gear1.photo is None:
                return self.gear2.photo.url
            else:  # 2 images
                if self.gear1.category.level >= self.gear2.category.level:
                    return self.gear1.photo.url
                else:
                    return self.gear2.photo.url

    def get_name(self):
        assert self.gear1 is not None

        if self.gear2 is None:
            return str(self.gear1)

        else:  # 2 images
            if self.gear1.category.level >= self.gear2.category.level:
                return str(self.gear1)
            else:
                return str(self.gear2)

    class Meta:
        verbose_name = 'Emprunt'
