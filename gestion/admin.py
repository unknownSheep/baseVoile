from django.contrib import admin
from .models import Gear, Adherent, GearCat, Rent


admin.site.register(Gear)
admin.site.register(GearCat)
admin.site.register(Adherent)
admin.site.register(Rent)
