from django.contrib import admin

# Register your models here.

from api.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'roll', 'city']