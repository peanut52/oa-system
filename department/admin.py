from django.contrib import admin
from department import models

# Register your models here.
admin.site.register(models.Department)
admin.site.register(models.Position)