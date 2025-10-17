from django.contrib import admin
from .models import Competition, Appearance, Grade

@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'location', 'organizer',
        'get_age_categories', 'get_style_categories', 'get_group_size_categories'
    )
    search_fields = ('date', 'location', 'description')
    list_filter = ('date', 'location')

    # Methods to display MultiSelectFields as comma-separated lists
    def get_age_categories(self, obj):
        return ", ".join(obj.age_categories)
    get_age_categories.short_description = 'Age Categories'

    def get_style_categories(self, obj):
        return ", ".join(obj.style_categories)
    get_style_categories.short_description = 'Style Categories'

    def get_group_size_categories(self, obj):
        return ", ".join(obj.group_size_categories)
    get_group_size_categories.short_description = 'Group Size Categories'


@admin.register(Appearance)
class AppearanceAdmin(admin.ModelAdmin):
    list_display = (
        'competition_id', 'club_manager', 'choreography', 'choreograph',
        'age_category', 'style_category', 'group_size_category'
    )
    search_fields = ('choreography', 'choreograph', 'competition__location')
    list_filter = ('age_category', 'style_category', 'group_size_category')


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'judge', 'appearance_id', 'grade'
    )
