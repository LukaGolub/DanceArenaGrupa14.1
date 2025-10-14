from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(
        regex=r'^\+?\s*(?:\d\s*){9,15}$',
        message="Enter a valid phone number: optional '+' followed by 9 to 15 digits. Spaces are allowed."
    )

class Administrator(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(validators=[phone_regex], max_length=20, blank=True)
    email = models.EmailField(max_length=50)

class Organizer(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(validators=[phone_regex], max_length=20, blank=True)
    email = models.EmailField(max_length=50)
    subscription_end = models.DateField()

class ClubManager(models.Model):
    name = models.CharField(max_length=50)
    club_name = models.CharField(max_length=50)
    club_location = models.CharField(max_length=50)
    contact = models.CharField(validators=[phone_regex], max_length=20, blank=True)
    email = models.EmailField(max_length=50)

class Judge(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(validators=[phone_regex], max_length=20, blank=True)
    email = models.EmailField(max_length=50)
