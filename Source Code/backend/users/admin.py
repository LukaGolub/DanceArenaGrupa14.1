from django.contrib import admin
from .models import Administrator, Organizer, ClubManager, Judge

class AdministratorAdmin(admin.ModelAdmin):
    list_display = \
        ('name', 'contact', 'email')
    search_fields = ('name', 'contact', 'email')
    list_filter = ('name', 'contact', 'email')

class OrganizerAdmin(admin.ModelAdmin):
    list_display = \
        ('name', 'contact', 'email')
    search_fields = ('name', 'contact', 'email')
    list_filter = ('name', 'contact', 'email')

class ClubManagerAdmin(admin.ModelAdmin):
    list_display = \
        ('name', 'contact', 'email')
    search_fields = ('name', 'contact', 'email')
    list_filter = ('name', 'contact', 'email')

class JudgeAdmin(admin.ModelAdmin):
    list_display = \
        ('name', 'contact', 'email')
    search_fields = ('name', 'contact', 'email')
    list_filter = ('name', 'contact', 'email')

admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(Organizer, OrganizerAdmin)
admin.site.register(ClubManager, ClubManagerAdmin)
admin.site.register(Judge, JudgeAdmin)