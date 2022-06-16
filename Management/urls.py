import imp
from django.urls import path
from .views.general_views.views import LogoutView,UserView,EmployeeView,RegisterView,InstitutionView,DepartmentView,JobTitleView,LoginView
from .views.driving_views.views import CourseView
from .views.general_views import views

urlpatterns = [
    path('hello/', views.HellowView.as_view(), name='hello'),
    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path('get_user',UserView.as_view()),
    path('logout',LogoutView.as_view()),
    path('institution/create',InstitutionView.as_view()),
    path('department/create',DepartmentView.as_view()),
    path('job-title/create',JobTitleView.as_view()),
    path('employee/create',EmployeeView.as_view()),
    path('couurse/create',CourseView.as_view())
]