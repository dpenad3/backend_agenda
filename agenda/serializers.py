from rest_framework import serializers
from .models import EducationLevel, Patient, ActivityType, ActivitiesPatient

class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = ('id', 'name', 'description')


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id','name', 'birth_date', 'ubication', 'cellphone', 'email', 'eps', 'rh', 'password', 'education_level')

class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = ('id', 'name', 'description')

class ActivitiesPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitiesPatient
        fields = ('id', 'name', 'activity_type', 'report', 'patient')
