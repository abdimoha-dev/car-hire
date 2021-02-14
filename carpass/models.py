from django.db import models

class Car(models.Model):
    def __str__(self):
        return self.car_numberplate
    
    car_model = models.CharField(max_length=50)
    car_numberplate = models.CharField(max_length=10)
    car_image = models.ImageField(upload_to = 'images', null=True, blank=True)
    car_sits = models.IntegerField()
    price_per_day = models.IntegerField()
    booked = models.BooleanField(default=False)
    booked_by = models.IntegerField(blank=True,null=True)
    # booked_by = models.