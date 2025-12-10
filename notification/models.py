from django.db import models
from cloudinary.models import CloudinaryField

class Village(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    post_code = models.CharField(max_length=20, default='0000')
    image = CloudinaryField('image')
    established_year = models.IntegerField(blank=True, null=True)
    head_of_village = models.CharField(max_length=100, blank=True, null=True)

    population = models.IntegerField(blank=True, null=True)
    total_voters = models.IntegerField(default=0)
    literacy_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    area_sq_km = models.FloatField(blank=True, null=True, help_text="Village area in square kilometers")
    number_of_houses = models.IntegerField(blank=True, null=True)
    number_of_schools = models.IntegerField(blank=True, null=True)
    number_of_health_centers = models.IntegerField(blank=True, null=True)
    number_of_markets = models.IntegerField(blank=True, null=True)
    number_of_religious_places = models.IntegerField(blank=True, null=True)
    number_of_community_centers = models.IntegerField(blank=True, null=True)

    has_electricity = models.BooleanField(default=True)
    has_clean_water = models.BooleanField(default=True)
    has_internet = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Notification: {self.message[:30]}"
    
