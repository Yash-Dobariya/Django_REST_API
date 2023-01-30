from rest_framework import serializers

class StudentSerializer(serializers.Serializer):

    id = serializers.ImageField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

