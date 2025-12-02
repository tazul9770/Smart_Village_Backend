from django.db import models
from django.conf import settings

class AgriculturedRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='agriculture_record')
    crop_name = models.CharField(max_length=100)
    land_size = models.CharField(max_length=20)
    yield_amount = models.FloatField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.crop_name
    
class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name

class Complain(models.Model):
    STATUS_CHOICES = (
        ('pending', 'PENDING'),
        ('resolved', 'RESOLVED'),
        ('rejected', 'REJECTED')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complains')
    tags = models.ManyToManyField(Tag, related_name='complaints', blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='complain_image/',blank=True, null=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
class ComplainResponse(models.Model):
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE, related_name='responses')
    responder = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    message = models.TextField()

    def __str__(self):
        return f"Response by {self.responder} on {self.complain.title}"
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField('event_image/', blank=True, null=True)
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="events")
    participant = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events')


    def __str__(self):
        return f"{self.name} ({self.date})"

