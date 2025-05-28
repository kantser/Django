from django.contrib import admin
from .models import Service, Project, TeamMember, ContactRequest

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin): # type: ignore
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin): # type: ignore
    list_display = ('title', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'created_at')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin): # type: ignore
    list_display = ('name', 'position', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'position')

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin): # type: ignore
    list_display = ('name', 'email', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_editable = ('is_processed',)
    date_hierarchy = 'created_at'
    actions = ['mark_as_processed']

    def mark_as_processed(self, request, queryset): # type: ignore
        queryset.update(is_processed=True) # type: ignore
    mark_as_processed.short_description = "Пометить как обработанные" # type: ignore