from django.contrib import admin
from django import forms

from .models import Discipline,Direction,StudentGroup,Document,Section,Theme,Employee,Department,Institute

# Register your models here.
@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name','slug','direction','department')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','institute','slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Direction)
class DirectionsAdmin(admin.ModelAdmin):
    list_display = ('name','code','slug','qualification','institute')   
    prepopulated_fields = {'slug': ('name',)} 

@admin.register(Institute)
class InstituteAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('doc_type','document')