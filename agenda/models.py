from django.db import models


class EducationLevel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    description = models.CharField(max_length=40, verbose_name='Descripción')

    def __str__(self):
        return self.name


class Patient(models.Model):
    RH = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-')
    ]

    name = models.CharField(max_length=50, verbose_name='Nombre')
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')
    ubication = models.CharField(max_length=30, verbose_name='Dirección')
    cellphone = models.CharField(max_length=15, unique=True, verbose_name='Celular')
    email = models.EmailField(max_length=50, unique=True, verbose_name='Correo')
    eps = models.CharField(max_length=20, verbose_name='Eps')
    rh = models.CharField(max_length=5, choices=RH, verbose_name='Rh')
    password = models.CharField(max_length=30, verbose_name='Contraseña')
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE, verbose_name='Nivel educativo')

    def __str__(self):
        return self.name


class ActivityType(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nombre')
    description = models.CharField(max_length=100, verbose_name='Descripción')

    def __str__(self):
        return self.name
        


class ActivitiesPatient(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nombre')
    activity_type = models.ForeignKey(ActivityType, on_delete=models.CASCADE, verbose_name='Tipo de actividad')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    date = models.DateField(verbose_name='Fecha de actividad')
    time = models.TimeField(verbose_name='Hora de actividad')
    image = models.ImageField(upload_to='report/images/', verbose_name='Imagen reporte', blank=True)
    record = models.FileField(upload_to='report/audio/', verbose_name='Audio reporte', blank=True)
    text = models.CharField(max_length=200, verbose_name='Texto reporte', blank=False)

    
    def __unicode__(self,):
        return str(self.image)

    def __str__(self):
        return "%s - %s" % (self.patient, self.name)
    
    