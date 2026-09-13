from django.db import models
from django.contrib.auth.models import AbstractUser
from user.manager import CustomUserManager
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    DESIGNATION_CHOICES = [
        ('bussinessman', 'Bussinessman'),
        ('entrepreneur', 'Entrepreneur'),
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
        ('housewife', 'Housewife')
    ]

    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    image = CloudinaryField('user_image', blank=True, null=True)
    designation = models.CharField(
        max_length=50,
        choices=DESIGNATION_CHOICES
    )
    bio = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
