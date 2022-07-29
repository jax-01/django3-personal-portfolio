from django.contrib import admin
from .models import Project

# Register your models here.

# i want to see Project model inside the admin
admin.site.register(Project)