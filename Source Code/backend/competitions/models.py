from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Age_choices(models.TextChoices):
    DJECA = "DJECA", "Djeca"
    JUNIORI = "JUNIORI", "Juniori"
    SENIORI = "SENIORI", "Seniori"


class Style_choices(models.TextChoices):
    BALET = "BALET", "Balet"
    HIPHOP = "HIPHOP", "Hip Hop"
    JAZZ = "JAZZ", "Jazz"
    STEP = "STEP", "Step"
    BREAK = "BREAK", "Break"


class Group_size_choices(models.TextChoices):
    SOLO = "SOLO", "Solo"
    DUO = "DUO", "Duo"
    MALA_GRUPA = "MALA_GRUPA", "Mala grupa"
    FORMACIJA = "FORMACIJA", "Formacija"


class Status_choices(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PUBLISHED = "PUBLISHED", "Published"
    CLOSED_APPLICATIONS = "CLOSED_APPLICATIONS", "Closed applications"
    ACTIVE = "ACTIVE", "Active"
    COMPLETED = "COMPLETED", "Completed"


class Competition(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'ORGANIZER'},
        on_delete=models.CASCADE,
        related_name='competitions'
    )
    age_categories = MultiSelectField(
        choices=Age_choices,
        max_choices=3,
        max_length=50,
        default=Age_choices.DJECA
    )
    style_categories = MultiSelectField(
        choices=Style_choices,
        max_choices=5,
        max_length=50,
        default=Style_choices.BALET
    )
    group_size_categories = MultiSelectField(
        choices=Group_size_choices,
        max_choices=4,
        max_length=50,
        default=Group_size_choices.SOLO
    )
    status = models.CharField(choices=Status_choices, max_length=20, default=Status_choices.DRAFT)
    starting_list_pdf = models.FileField(
        upload_to='starting_lists/',
        blank=True,
        null=True
    )
    registration_fee = models.DecimalField(decimal_places=2, max_digits=6, default=0)

    def __str__(self):
        return f"""ID:{self.id}-ORGANIZER:{self.organizer}-  
                AGE CATEGORIES:{self.age_categories}-
                STYLE CATEGORIES:{self.style_categories}-
                GROUP SIZE CATEGORIES:{self.group_size_categories}
                ====================
                """


class Competition_Judge(models.Model):
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name='competition_judges'
    )
    judge = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'JUDGE'},
        on_delete=models.CASCADE,
        related_name='assigned_competitions'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['judge','competition'], name='unique_judge_competition')
        ]

    def __str__(self):
        return f"""{self.judge.username}->{self.competition}
                ===================="""


class Appearance(models.Model):
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name='appearances'
    )
    club_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'CLUB MANAGER'},
        on_delete=models.CASCADE,
        related_name='appearances',
        null=True
    )
    choreography = models.CharField(max_length=50)
    length = models.DurationField()
    choreograph = models.CharField(max_length=50)
    music = models.FileField(null=True, blank=True)
    age_category = models.CharField(
        max_length=50,
        choices=Age_choices,
        default=Age_choices.DJECA
    )
    style_category = models.CharField(
        max_length=50,
        choices=Style_choices,
        default=Style_choices.BALET
    )
    group_size_category = models.CharField(
        max_length=50,
        choices=Group_size_choices,
        default=Group_size_choices.SOLO
    )
    paid_registration = models.BooleanField(default=False)

    def __str__(self):
        return f"""ID:{self.id}-COMPETITION ID:{self.competition.id}-
                CLUB MANAGER:{self.club_manager}-
                AGE CATEGORY:{self.age_category}-
                STYLE CATEGORY:{self.style_category}-
                GROUP SIZE CATEGORY:{self.group_size_category}
                ====================
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

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['judge','appearance'], name='unique_judge_appearance')
        ]

    def __str__(self):
        return f"""{self.judge.username}->{self.appearance.id}:{self.grade}
                ===================="""


