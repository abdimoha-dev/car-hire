from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','car_model','car_numberplate', 'car_sits','price_per_day','booked','booked_by']
        # fields = '__all__'
        