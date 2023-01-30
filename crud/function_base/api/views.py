from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_api(request):

    # Read
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id', None)

        if id is None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type = 'application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type = 'application/json')

    # Create
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data= python_data)

        if serializer.is_valid():
            serializer.save()
            res = {"msg":"data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = '/application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = '/application/json')

    # Update
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id=python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data= python_data, partial = True)

        if serializer.is_valid():
            serializer.save()
            res = {"msg": "data updated"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')

        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type = 'application/json')

    # Delete
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {"mes": "data deleted"}
        json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type = 'application/json')

    