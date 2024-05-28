from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Job, Candidate

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'representative_name', 'created_at', 'updated_at')
    search_fields = ('name', 'representative_name')
    list_filter = ('created_at', 'updated_at')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'customer', 'location', 'created_at', 'updated_at')
    search_fields = ('name', 'status', 'customer__name', 'location')
    list_filter = ('status', 'created_at', 'updated_at')

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'skills')
    list_filter = ('created_at', 'updated_at')