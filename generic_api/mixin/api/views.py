from api.models import Student
from api.serializer import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class LCStudent(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    """function for get all data"""
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


    """function for create data"""
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 
    
class RUDStudent(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)