from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, NewEmployeeViewSet
from django.conf import settings
from django.conf.urls.static import static

# Create a router for the API views
router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'person', NewEmployeeViewSet)

urlpatterns = [
    # Define the default API URL patterns using the router
    path('', include(router.urls)),
    path('api/', include(router.urls)),

    # # Custom URL patterns for single fetch and bulk fetch
    # path('api/companies/', CompanyViewSet.as_view({'get': 'list'}), name='company-list'),
    # path('api/companies/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve'}), name='company-detail'),

    # path('api/employees/', EmployeeViewSet.as_view({'get': 'list'}), name='employee-list'),
    # path('api/employees/<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve'}), name='employee-detail'),

    # # Custom URL patterns for NewEmployee
    # path('api/new-employees/', NewEmployeeViewSet.as_view({'get': 'list'}), name='new-employee-list'),
    # path('api/new-employees/<int:pk>/', NewEmployeeViewSet.as_view({'get': 'retrieve'}), name='new-employee-detail'),

    # Include DRF's login/logout views if needed
    path('api-auth/', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
