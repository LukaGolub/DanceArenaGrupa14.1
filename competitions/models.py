from django.db import models

class AgeCategory(models.Model):
    age_categories = [
        ('DJECA', 'djeca'),
        ('JUNIORI', 'juniori'),
        ('SENIORI', 'seniori')
    ]
    age_category = models.CharField(
        max_length=20,
        choices=age_categories,
        unique=True
    )

class StyleCategory(models.Model):
    style_categories = [
        ('BALET', 'balet'),
        ('HIP HOP', 'hip hop'),
        ('JAZZ', 'jazz'),
        ('STEP', 'step'),
        ('BREAK', 'break')
    ]
    style_category = models.CharField(
        max_length=20,
        choices=style_categories,
        unique=True
    )

class GroupSizeCategory(models.Model):
    group_size_categories = [
        ('SOLO', 'solo'),
        ('DUO', 'duo'),
        ('MALA GRUPA', 'mala grupa'),
        ('FORMACIJA', 'formacija')
    ]
    group_size_category = models.CharField(
        max_length=20,
        choices=group_size_categories,
        unique=True
    )

class Competition(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    age_categories = models.ManyToManyField(AgeCategory)
    style_categories = models.ManyToManyField(StyleCategory)
    group_size_categories = models.ManyToManyField(GroupSizeCategory)


