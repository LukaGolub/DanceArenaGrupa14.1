from django.db import models
from multiselectfield import MultiSelectField
from users.models import Organizer

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

class Competition(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    organizer = models.ForeignKey(
        Organizer,
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

    def __str__(self):
        return f"{self.location} ({self.date})"


class Appearance(models.Model):
    competition = models.ForeignKey(
        Competition,
        on_delete=models.CASCADE,
        related_name='appearances'
    )
    choreography = models.CharField(max_length=50)
    length = models.TimeField()
    choreograph = models.CharField(max_length=50)
    music = models.FileField()
    age_category = models.CharField(
        max_length=50,
        choices=AGE_CHOICES,
        default='DJECA'
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
