from django.contrib import admin
from .models import Company, Employee,CustomUser,NewEmployee

# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(CustomUser)
admin.site.register(NewEmployee)