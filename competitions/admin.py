from django.contrib import admin
from .models import Competition, Appearance

class CompetitionAdmin(admin.ModelAdmin):
    list_display = \
        ('date', 'location', 'organizer', 'age_categories',
         'style_categories', 'group_size_categories')
    search_fields = ('date', 'location', 'description')
    list_filter = ('date', 'location')

    def get_age_categories(self, obj):
        return ", ".join(obj.age_categories)

    get_age_categories.short_description = 'Age Categories'

    def get_style_categories(self, obj):
        return ", ".join(obj.style_categories)

    get_style_categories.short_description = 'Style Categories'

    def get_group_size_categories(self, obj):
        return ", ".join(obj.group_size_categories)

    get_group_size_categories.short_description = 'Group Size Categories'

class AppearanceAdmin(admin.ModelAdmin):
    list_display = \
        ('competition', 'choreography', 'choreograph',
         'age_category', 'style_category', 'group_size_category')
    search_fields = ('choreography', 'choreograph')
    list_filter = ('choreography', 'choreograph')


admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Appearance, AppearanceAdmin)


