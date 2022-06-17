import imp
from django.urls import path
from .views.general_views.views import LogoutView,UserView,EmployeeView,RegisterView,InstitutionView,DepartmentView,JobTitleView,LoginView
from .views.driving_views.views import CourseView, NtsaView
from .views.general_views import views
from .views.general_views.get_views import GetInstitutionView,GetDepartmentView,GetJobTititletView,GetEmployeeView,GetUserView
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
    path('course/create',CourseView.as_view()),
    path('ntsa/create',NtsaView.as_view()),

    path('institution/get',GetInstitutionView.as_view()),
    path('department/get',GetDepartmentView.as_view()),
    path('jobs/get',GetJobTititletView.as_view()),
    path('employee/get',GetEmployeeView.as_view()),
    path('users/get',GetUserView.as_view())
]
