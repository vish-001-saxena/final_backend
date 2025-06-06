from django.db import models

# Create your models here.
#use to write structure 

class Student(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    # image=models.ImageField()
    # field=models.FieldFile()

#  product(models.Model):
#     pass
# class


class Car(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.car_name