from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('programs/', views.program_list, name='programs'),
    path('programs/<int:id>/', views.program_detail, name='program_detail'),
    path('departments/', views.department_list, name='departments'),
    path('departments/<int:id>/', views.department_detail, name='department_detail'),
    path('exchange/', views.exchange_list, name='exchange'),
]