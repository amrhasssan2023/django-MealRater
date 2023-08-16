from django.shortcuts import render
from rest_framework import viewsets
from .models import Meal, Rate
from .serializers import MealSerializer, RateSerializer,UserSerializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated , IsAdminUser, IsAuthenticatedOrReadOnly



# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = []
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']




class Mealviewsets(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def rate_meal(self, request, pk=None):

        meal = Meal.objects.get(id=pk)
        starts = request.data['stars']
        user = request.user
        #username = request.data['username']
        #user = User.objects.get(username=username)

        if 'stars' in request.data:
            #update
            try:
                rating = Rate.objects.get(meal = meal.id, user=user.id)
                rating.stars = starts
                rating.save
                serializer = RateSerializer(rating, many= False)
                json = {
                    'message' : 'Meal are updated',
                    'result' : serializer.data
                }
                return Response(json, status=status.HTTP_200_OK)
            except:
                rating = Rate.objects.create(meal = meal.id, starts= starts.id, user=user)
                serializer = RateSerializer(rating, many= False)
                json = {
                    'massage' : 'Meal are created',
                    'result' : serializer.data
                }
                return Response(json, status=status.HTTP_201_CREATED)
            
        else:
            json={
                'message' : 'starts not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)




class Rateviewsets(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['meal']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        response = {
            'message' : 'invalid way to create or update'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
        response = {
            'message' : 'invalid way to create or update'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    