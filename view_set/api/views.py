from django.shortcuts import render
from rest_framework import viewsets, status
from api.models import Student
from api.serialize import StudentSerialize
from rest_framework.response import Response

# Create your views here.

class StudentViewSet(viewsets.ViewSet):

    def get(self, request):
        stu = Student.objects.all()
        serializer = StudentSerialize(stu, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerialize(stu)
            return Response(serializer.data)
    
    def create(self, request):
        serializer = StudentSerialize(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data Created"}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerialize(stu, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Data Update"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerialize(stu, data= request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Partial Data update"}, status= status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self, request,pk):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg":"Data Delete"})
