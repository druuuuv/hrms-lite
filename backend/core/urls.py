from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import EmployeeViewSet, AttendanceViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html')),
]