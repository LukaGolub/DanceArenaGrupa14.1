from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

AGE_CHOICES = [
    ('DJECA', 'Djeca'),
    ('JUNIORI', 'Juniori'),
    ('SENIORI', 'Seniori'),
]

STYLE_CHOICES = [
    ('BALET', 'Balet'),
    ('HIPHOP', 'Hip Hop'),
    ('JAZZ', 'Jazz'),
    ('STEP', 'Step'),
    ('BREAK', 'Break'),
]

GROUP_SIZE_CHOICES = [
    ('SOLO', 'Solo'),
    ('DUO', 'Duo'),
    ('MALA_GRUPA', 'Mala grupa'),
    ('FORMACIJA', 'Formacija'),
]

STATUS_CHOICES = [
    ('DRAFT', 'Draft'),
    ('PUBLISHED', 'Published'),
    ('CLOSED_APPLICATIONS', 'Closed_applications'),
    ('ACTIVE', 'Active'),
    ('COMPLETED', 'Completed')
]


class Meta:
    constraints = [
        models.UniqueConstraint(fields=['judge', 'appearance'], name='unique_judge_appearance')
    ]


class Competition(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'ORGANIZER'},
        on_delete=models.CASCADE,
        related_name='competitions',
        null=True
    )
    age_categories = MultiSelectField(
        choices=AGE_CHOICES,
        max_choices=3,
        max_length=50,
        default=['DJECA']
    )
    style_categories = MultiSelectField(
        choices=STYLE_CHOICES,
        max_choices=5,
        max_length=50,
        default=['BALET']
    )
    group_size_categories = MultiSelectField(
        choices=GROUP_SIZE_CHOICES,
        max_choices=4,
        max_length=50,
        default=['SOLO']
    )
    status = models.CharField(max_length=10, default='draft')

    def __str__(self):
        return f"""ID:{self.id}-ORGANIZER:{self.organizer}-LOCATION:{self.location}-
                DATE:{self.date}-STATUS:{self.status}-  
                AGE CATEGORIES:{self.age_categories}-
                STYLE CATEGORIES:{self.style_categories}-
                GROUP SIZE CATEGORIES:{self.group_size_categories}
                ===========================================================
                """


class Appearance(models.Model):
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name='appearances'
    )
    club_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'CLUB_MANAGER'},
        on_delete=models.CASCADE,
        related_name='appearances',
        null=True
    )
    choreography = models.CharField(max_length=50)
    length = models.TimeField()
    choreograph = models.CharField(max_length=50)
    music = models.FileField()
    age_category = models.CharField(
        max_length=50,
        choices=AGE_CHOICES,
        default='DJECA',
    )
    style_category = models.CharField(
        max_length=50,
        choices=STYLE_CHOICES,
        default='BALET'
    )
    group_size_category = models.CharField(
        max_length=50,
        choices=GROUP_SIZE_CHOICES,
        default='SOLO'
    )

    def competition_id(self):
        return self.competition.id
    competition_id.short_description = 'Competition ID'

    def __str__(self):
        return f"""ID:{self.id}-COMPETITION ID:{self.competition.id}-
                CLUB MANAGER:{self.club_manager}-CHOREOGRAPHY:{self.choreography}-
                CHOREOGRAPH:{self.choreograph}-
                AGE CATEGORY:{self.age_category}-
                STYLE CATEGORY:{self.style_category}-
                GROUP SIZE CATEGORy:{self.group_size_category}
                ===========================================================
                """


class Grade(models.Model):
    judge = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'JUDGE'},
        on_delete=models.CASCADE,
        related_name='grades'
    )
    appearance = models.ForeignKey(
        Appearance,
        on_delete=models.CASCADE,
        related_name='grades'
    )
    grade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(30)]
    )

    def appearance_id(self):
        return self.appearance.id
    appearance_id.short_description = 'Appearance ID'


