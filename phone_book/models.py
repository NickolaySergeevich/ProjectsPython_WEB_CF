from django.db import models


class PhoneBook(models.Model):
    contact_name = models.TextField()
    contact_surname = models.TextField()
    contact_phone = models.IntegerField()
    contact_notes = models.TextField()
