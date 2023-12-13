from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Company, Employee,NewEmployee
from .serializers import CompanySerializer, EmployeeSerializer,NewEmployeeSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows authenticated users full access, read-only for others

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows authenticated users full access, read-only for others

class NewEmployeeViewSet(viewsets.ModelViewSet):
    queryset = NewEmployee.objects.all()
    serializer_class = NewEmployeeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows authenticated users full access, read-only for others
