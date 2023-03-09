from django.contrib import admin
from .models import Profile

# Register your models here.

# admin.site.register(Profile)  -> Modelda nimalar berilgan bo'lsa hammasi chiqadi

class ProfileAdmin(admin.ModelAdmin):  # Biz list_desplayda bergan fieldlarni chiqarib beradi
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Profile , ProfileAdmin)   

# make migrations qilish esdan chiqmasin


