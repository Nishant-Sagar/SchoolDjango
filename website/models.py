from django.db import models

# Create your models here.
class Admission(models.Model):
    name  = models.CharField(max_length= 100)
    father_name = models.CharField(max_length= 100)
    guardian_name = models.CharField(max_length= 100)
    occupation = models.CharField(max_length= 100)
    dob = models.DateField()
    phone = models.IntegerField()
    email = models.EmailField(max_length= 100)
    qualification = models.CharField(max_length= 100)
    address = models.TextField(max_length= 100)
    city = models.CharField(max_length= 100)
    pincode = models.IntegerField()
    religion = models.CharField(max_length= 100)
    sex  = models.CharField(max_length= 10)
    nationality = models.CharField(max_length= 10)

    def __str__(self):
        return self.name