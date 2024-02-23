from django.db import models


class PhoneBook(models.Model):
    contact_name = models.TextField()
    contact_surname = models.TextField()
    contact_phone = models.TextField()
    contact_notes = models.TextField()
