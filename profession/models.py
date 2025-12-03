from django.db import models
from django.conf import settings

class ProfessionUser(models.Model):
    PROFESSION_CHOICES = [
        ('bussinessman','Bussinessman'),
        ('software_engineer', 'Software Engineer'),
        ('software_developer', 'Software Developer'),
        ('freelancer', 'Freelancer'),
        ('teacher', 'Teacher'),
        ('doctor', 'Doctor'),
        ('student', 'Student'),
        ('nurse', 'Nurse'),
        ('farmer', 'Farmer'),
        ('mechanic', 'Mechanic'),
        ('designer', 'Designer'),
        ('data_scientist', 'Data Scientist'),
        ('defense', 'Defense'),
        ('lawyer', 'Lawyer'),
        ('accountant', 'Accountant'),
        ('artist', 'Artist'),
        ('chef', 'Chef'),
        ('photographer', 'Photographer'),
        ('journalist', 'Journalist'),
        ('driver', 'Driver'),
        ('pilot', 'Pilot'),
        ('engineer', 'Engineer'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profession_profile')
    age = models.IntegerField()
    image = models.ImageField(upload_to='profession_image/', blank=True, null=True)
    description = models.TextField()
    profession = models.CharField(max_length=50, choices=PROFESSION_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.get_profession_display()})"

