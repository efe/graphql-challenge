# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from celebrityshop.ingredients.models import Category, Ingredient

admin.site.register(Category)
admin.site.register(Ingredient)
