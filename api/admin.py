from django.contrib import admin
from .models import Meal, Rate

# Register your models here.
class MealAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    search_fields = ['title','description']
    list_filter = ['title','description']

class ReteAdmin(admin.ModelAdmin):
    list_display = ['id','user','meal','stars']
    search_fields = ['user','meal','stars']
    list_filter = ['user','meal','stars']


admin.site.register(Meal,MealAdmin)
admin.site.register(Rate,ReteAdmin)