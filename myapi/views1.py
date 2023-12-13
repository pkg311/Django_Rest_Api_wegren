from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.permissions import IsAuthenticated

# ViewSet for Company model
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

    # Additional custom action
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        company = self.get_object()
        employees = company.employee_set.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

# ViewSet for Employee model with mixins for specific actions
class EmployeeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Company, Employee
# from .serializers import CompanySerializer, EmployeeSerializer
# from django.shortcuts import get_object_or_404

# # View for handling Company model
# class CompanyAPIView(APIView):
#     def get(self, request, company_id=None):
#         if company_id:
#             company = get_object_or_404(Company, pk=company_id)
#             serializer = CompanySerializer(company)
#             return Response(serializer.data)
#         else:
#             companies = Company.objects.all()
#             serializer = CompanySerializer(companies, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, company_id=None):
#         company = get_object_or_404(Company, pk=company_id)
#         serializer = CompanySerializer(company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, company_id=None):
#         company = get_object_or_404(Company, pk=company_id)
#         company.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# # View for handling Employee model
# class EmployeeAPIView(APIView):
#     def get(self, request, employee_id=None):
#         if employee_id:
#             employee = get_object_or_404(Employee, pk=employee_id)
#             serializer = EmployeeSerializer(employee)
#             return Response(serializer.data)
#         else:
#             employees = Employee.objects.all()
#             serializer = EmployeeSerializer(employees, many=True)
#             return Response(serializer.data)

#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, employee_id=None):
#         employee = get_object_or_404(Employee, pk=employee_id)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, employee_id=None):
#         employee = get_object_or_404(Employee, pk=employee_id)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
