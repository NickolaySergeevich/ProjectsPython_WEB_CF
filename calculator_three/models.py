from django.db import models


class CalculatorHistory(models.Model):
    number_one = models.IntegerField()
    number_two = models.IntegerField()
    answer = models.IntegerField()
