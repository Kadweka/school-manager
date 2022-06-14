from django.urls import path
from .views import RegisterView,InstitutionView
from . import views

urlpatterns = [
    path('hello/', views.HellowView.as_view(), name='hello'),
    path('register',RegisterView.as_view()),
    path('institution/create',InstitutionView.as_view())
]