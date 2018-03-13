from django.shortcuts import render
from .serializers import UserSerializer
from .models import User
import datetime
from rest_framework_mongoengine import viewsets

class UserViewSet(viewsets.ModelViewSet):
	# lookup_field = 'id'
	serializer_class = UserSerializer

	def get_queryset(self):
		return User.objects.all()
