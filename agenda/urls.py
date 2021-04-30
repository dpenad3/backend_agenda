from django.urls import path
from agenda import views

urlpatterns = [
    path('levels/', views.education_Level_List),
    path('levels/<int:pk>/', views.education_Level_detail),
    path('patients/', views.patient_List),
    path('patients/<int:pk>/', views.patient_detail),
    path('activitiestype/', views.activity_type_List),
    path('activitiestype/<int:pk>/', views.activity_type_detail),
    path('activitiespatient/', views.activities_patient_List),
    path('activitiespatient/<int:pk>', views.activities_patient_detail),
]
