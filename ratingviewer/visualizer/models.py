from django.db import models

# Create your models here.
class Members(models.Model):
    id = models.AutoField(primary_key=True)
    ncs_id = models.CharField(max_length=20)
    name_alphabet = models.CharField(max_length=256)
    name_kanji = models.CharField(max_length=256)
    
class Ratings(models.Model):
    id = models.AutoField(primary_key=True)
    ncs_id = models.CharField(max_length=20)
    rating = models.IntegerField()
    update_month = models.DateField()