from api.models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student
        fields = ['id', 'name', 'roll', 'city']