from rest_framework import serializers
from .models import Meal, Rate,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id','title','description','number_of_rate', 'avg_rating']

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['id','user','meal','stars']

