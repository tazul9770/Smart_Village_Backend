from django.db import models
from user.models import User

class Institution(models.Model):
    SCHOOL = 'school'
    COLLEGE = 'college'
    UNIVERSITY = 'university'

    INSTITUTION_TYPES = [
        (SCHOOL, 'School'),
        (COLLEGE, 'College'),
        (UNIVERSITY, 'University'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=20,
        choices=INSTITUTION_TYPES,
        default=SCHOOL
    )
    address = models.TextField()
    image = models.ImageField(upload_to='institute_image/', blank=True, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    image = models.ImageField(upload_to='student_image/', blank=True, null=True)
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Clinik(models.Model):
    GOVT = 'government'
    PRIVATE = 'private'
    NGO = 'ngo'

    CLINIK_TYPES = [
        (GOVT, 'Government'),
        (PRIVATE, 'Private'),
        (NGO, 'NGO'),
    ]

    name = models.CharField(max_length=100)
    address = models.TextField()
    image = models.ImageField(upload_to='clinik_image/', blank=True, null=True)
    type = models.CharField(
        max_length=20,
        choices=CLINIK_TYPES,
        default=PRIVATE
    )

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    
class Doctor(models.Model):
    clinik = models.ForeignKey(Clinik, on_delete=models.CASCADE, related_name='doctor')
    name = models.CharField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='doctor_image/', blank=True, null=True)
    specialization = models.CharField()

class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="businesses")
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    revenue = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Profession(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProfessionUser(models.Model):
    name = models.CharField(max_length=100)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, related_name="users")

    def __str__(self):
        return f"{self.name} ({self.profession})"
