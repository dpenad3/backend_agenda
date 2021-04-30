from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import EducationLevel, Patient, ActivityType, ActivitiesPatient
from .serializers import EducationLevelSerializer, PatientSerializer, ActivityTypeSerializer, ActivitiesPatientSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def education_Level_List(request):
    if request.method == 'GET':
        levels = EducationLevel.objects.all()
        serializer = EducationLevelSerializer(levels, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EducationLevelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def education_Level_detail(request, pk):
    try:
        level = EducationLevel.objects.get(pk=pk)
    except EducationLevel.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EducationLevelSerializer(level)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EducationLevelSerializer(level, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        level.delete()
        return HttpResponse(status=204)


@csrf_exempt
def patient_List(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def patient_detail(request, pk):
    try:
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(patient, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        patient.delete()
        return HttpResponse(status=204)


@csrf_exempt
def activity_type_List(request):
    if request.method == 'GET':
        types = ActivityType.objects.all()
        serializer = ActivityTypeSerializer(types, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivityTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def activity_type_detail(request, pk):
    try:
        activity = ActivityType.objects.get(pk=pk)
    except ActivityType.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ActivityTypeSerializer(activity)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ActivityTypeSerializer(activity, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        activity.delete()
        return HttpResponse(status=204)


@csrf_exempt
def activities_patient_List(request):
    if request.method == 'GET':
        activities_patient = ActivitiesPatient.objects.all()
        serializer = ActivitiesPatientSerializer(activities_patient, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ActivitiesPatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def activities_patient_detail(request, pk):
    try:
        activities = ActivitiesPatient.objects.get(pk=pk)
    except ActivitiesPatient.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ActivitiesPatientSerializer(activities)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ActivitiesPatientSerializer(activities, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        activities.delete()
        return HttpResponse(status=204)
