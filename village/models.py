from django.db import models
from django.conf import settings
    
class Complain(models.Model):
    TAG_CHOICES = [
        ('road_issue', 'Road Issue'),
        ('electricity', 'Electricity'),
        ('water_supply', 'Water Supply'),
        ('garbage', 'Garbage Problem'),
        ('traffic', 'Traffic Jam'),
        ('street_light', 'Street Light'),
        ('internet', 'Internet Issue'),
        ('gas', 'Gas Problem'),
        ('drainage', 'Drainage Issue'),
        ('public_safety', 'Public Safety'),
        ('other', 'Other')
    ]

    STATUS_CHOICES = (
        ('pending', 'PENDING'),
        ('resolved', 'RESOLVED'),
        ('rejected', 'REJECTED')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='complains') 
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='complain_image/', blank=True, null=True)
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
    
class Event(models.Model):

    CATEGORY_CHOICES = [
        ('cultural', 'Cultural Event'),
        ('sports', 'Sports Event'),
        ('religious', 'Religious Event'),
        ('education', 'Educational Program'),
        ('health', 'Health Camp'),
        ('festival', 'Village Festival'),
        ('meeting', 'Public Meeting'),
        ('training', 'Training Workshop'),
        ('youth', 'Youth Program'),
        ('awareness', 'Awareness Campaign'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='event_image/', blank=True, null=True)
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    participant = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='events')
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('upcoming','Upcoming'),('completed','Completed')], default='upcoming')
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_events')

    def __str__(self):
        return f"{self.name}"


