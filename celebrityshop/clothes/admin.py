from django.contrib import admin

from celebrityshop.clothes.models import Celebrity, Cloth

admin.site.register(Cloth)
admin.site.register(Celebrity)
