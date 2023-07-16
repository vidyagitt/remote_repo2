from django.db import models

class HydJobs(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=35)
    eligibility=models.CharField(max_length=30)
    adderess=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class BangaluruJobs(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=35)
    eligibility=models.CharField(max_length=30)
    adderess=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class ChennaiJobs(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=35)
    eligibility=models.CharField(max_length=30)
    adderess=models.CharField(max_length=50)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

