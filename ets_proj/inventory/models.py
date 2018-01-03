from django.db import models
from django.core.urlresolvers import reverse

class Equipment(models.Model):
    tnumber = models.CharField(max_length=20)
    brand = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    category = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    manual = models.CharField(max_length=256)
    status = models.CharField(max_length=256)
    purchased_date = models.DateField(max_length=256)

    def __str__(self):
        return self.tnumber

    def get_absolute_url(self):
        return reverse("inventory:detail", kwargs={'pk':self.pk})

class Calibration(models.Model):
    tnumber = models.ForeignKey(Equipment)
    calibration_date = models.DateField(max_length=256)

    def __str__(self):
        return str(self.tnumber)

class Warranty(models.Model):
    tnumber = models.ForeignKey(Equipment)
    warranty_start_date = models.DateField(max_length=256)
    warranty_end_date = models.DateField(max_length=256)

    def __str__(self):
        return str(self.tnumber)
