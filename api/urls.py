from django.urls import path, include
from .views import Mealviewsets,Rateviewsets,UserViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('user',UserViewset)
router.register('meal', Mealviewsets)
router.register('rate',Rateviewsets)


urlpatterns = [ 
    path('api-viewsets',include(router.urls)),
    path('api-auth',include('rest_framework.urls')),
    path('api-auth-token',obtain_auth_token)

]