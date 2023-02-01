from django.shortcuts import render
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, 
                                    ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView,
                                    RetrieveUpdateDestroyAPIView)
from api.models import Student
from api.serializer import StudentSerializer

# Create your views here.

class LCStudent(ListAPIView, CreateAPIView):

    queryset = Student.objects.all()
    serializer_class =  StudentSerializer

class RUDStudent(RetrieveAPIView, UpdateAPIView, DestroyAPIView):

    queryset = Student.objects.all()
    serializer_class =  StudentSerializer    