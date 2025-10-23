from django.contrib import admin
from .models import Competition, Appearance, Grade, Competition_Judge


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'date', 'location', 'organizer', 'status', 'registration_fee',
        'get_age_categories', 'get_style_categories', 'get_group_size_categories'
    )
    search_fields = ('date', 'location', 'description')
    list_filter = ('date', 'location')
    ordering = ('date', 'id')

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
        'id', 'competition_info', 'club_manager__username', 'paid_registration', 
        'choreography', 'choreograph',
        'age_category', 'style_category', 'group_size_category'
    )
    search_fields = (
        'club_manager', 'choreography', 'choreograph', 'competition'
        )
    list_filter = (
        'club_manager', 'paid_registration', 
        'age_category', 'style_category', 'group_size_category'
    )
    ordering = ('club_manager', 'id')

    def competition_info(self, obj):
        return f"{obj.competition.id} - {obj.competition.location}"
    competition_info.short_description = 'Competition'

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'competition_info', 'judge_info', 'appearance_id', 'grade'
    )
    list_filter = ('appearance__id', 'grade')
    search_fields = ('appearance__id', 'grade')
    ordering = ('id',)

    def competition_info(self, obj):
        return f"{obj.appearance.competition.id} - {obj.appearance.competition.location}"
    competition_info.short_description = 'Competition'

    def judge_info(self, obj):
        return f"{obj.judge.id} - {obj.judge.username}"
    judge_info.short_description = 'Judge'

    def appearance_id(self, obj):
        return obj.appearance.id
    appearance_id.short_description = 'Appearance ID'


@admin.register(Competition_Judge)
class Competition_JudgeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'judge_info', 'competition_info'
    )
    list_filter = ('judge', 'competition')
    search_fields = ('judge', 'competition')
    ordering = ('competition', 'id')

    def judge_info(self, obj):
        return f"{obj.judge.id} - {obj.judge.username}"
    judge_info.short_description = 'Judge'

    def competition_info(self, obj):
        return f"{obj.competition.id} - {obj.competition.location}"
    competition_info.short_description = 'Competition'