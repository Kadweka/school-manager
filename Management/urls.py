from django.urls import path
from .views import EmployeeView,RegisterView,InstitutionView,DepartmentView,JobTitleView
from . import views

urlpatterns = [
    path('hello/', views.HellowView.as_view(), name='hello'),
    path('register',RegisterView.as_view()),
    path('institution/create',InstitutionView.as_view()),
    path('department/create',DepartmentView.as_view()),
    path('job-title/create',JobTitleView.as_view()),
    path('employee/create',EmployeeView.as_view())
]