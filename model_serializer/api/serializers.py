from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:

        model = Student
        fields = ['id', 'name', 'roll', 'city']

        # read_only_fields & extra_kwarg is use to no changes mention fields in update method
        read_only_fields = ['name', 'roll']
        extra_kwargs = {'name':{'read_only': True}}