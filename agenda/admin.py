from django.contrib import admin
from agenda.models import Patient, EducationLevel, ActivitiesPatient, ActivityType

admin.site.register(Patient)
admin.site.register(EducationLevel)
admin.site.register(ActivityType)
admin.site.register(ActivitiesPatient)
