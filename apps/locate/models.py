from doctest import BLANKLINE_MARKER
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from sqlalchemy import null

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Info(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    operating_hours = models.TextField(null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length= 50, blank=True, null=True)

    def __str__(self):
        return self.name

class Coupon(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    coupon_type = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    shop = models.CharField(max_length= 50, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True)
    code = models.TextField()
    quantity = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name