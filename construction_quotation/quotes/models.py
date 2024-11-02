from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Project(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('DECLINED', 'Declined'),
        ('COMPLETED', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    area_size = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Element(models.Model):
    name = models.CharField(max_length=255)


class Material(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.CharField(max_length=50, default='N/A')  # Ensure default is set if needed
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    markup_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Quotation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()