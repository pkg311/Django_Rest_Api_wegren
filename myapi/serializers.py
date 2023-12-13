from rest_framework import serializers
from .models import Company, Employee, NewEmployee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'  # Serialize all fields in the Company model

    # Validation for fields (Example: Custom validation for the name field)
    def validate_name(self, value):
        # Add your custom validation logic for the name field
        if not value.isalpha():
            raise serializers.ValidationError("Company name must contain only alphabetic characters.")
        return value

    # Field-level representation (Example: Custom representation for the location field)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['location'] = instance.location.upper()  # Represent location in uppercase
        return representation
    
    
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # Serialize all fields in the Employee model

    # Validation for fields (Example: Custom validation for the email field)
    def validate_email(self, value):
        # Add your custom validation logic for the email field
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError("Email must be from gmail.com domain.")
        return value

    # Field-level representation (Example: Custom representation for the phone field)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['phone'] = f"+{instance.phone}"  # Represent phone number with a prefix '+'
        return representation


class NewEmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewEmployee
        fields = '__all__'
