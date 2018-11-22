# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Calendar(models.Model):
    date = models.DateField(primary_key=True)
    dow = models.CharField(max_length=16, blank=True, null=True)
    year_lunar = models.IntegerField(blank=True, null=True)
    month_lunar = models.CharField(max_length=16, blank=True, null=True)
    day_lunar = models.CharField(max_length=16, blank=True, null=True)
    year_branch = models.CharField(max_length=16, blank=True, null=True)
    zodiac = models.CharField(max_length=8, blank=True, null=True)
    leap_month = models.IntegerField(blank=True, null=True)
    month_branch = models.CharField(max_length=16, blank=True, null=True)
    day_branch = models.CharField(max_length=16, blank=True, null=True)
    solar_period = models.CharField(max_length=8, blank=True, null=True)
    solar_period_time = models.TimeField(blank=True, null=True)
    holiday = models.CharField(max_length=255, blank=True, null=True)
    holiday_lunar = models.CharField(max_length=32, blank=True, null=True)
    holiday_special = models.CharField(max_length=32, blank=True, null=True)
    hot_summer_days = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar'
