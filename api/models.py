from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Meal(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250)

    def number_of_rate(self):
        rating = Rate.objects.filter(meal=self)
        return len(rating)

    def avg_rating(self):
        sum = 0
        rating = Rate.objects.filter(meal=self)

        for x in rating:
            sum += x.stars
        
        if len(rating) > 0:
            return  sum / len(rating)    
        else:
            return 0
  


    def __str__(self):
        return self.title
    
class Rate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return str(self.meal)
    
    class Meta:
        unique_together = (('user'),('meal'),)
        index_together = (('user'),('meal'),)