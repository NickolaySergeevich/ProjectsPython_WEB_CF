from django.db import models


class Notes(models.Model):
    note_header = models.TextField()
    note_description = models.TextField()


class NotesSupplements(models.Model):
    note_id = models.ForeignKey(Notes, on_delete=models.CASCADE)
    note_supplement = models.TextField()
