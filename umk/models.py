from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime 
import os

class Institute(models.Model):
    name = models.CharField(max_length=250)
    info = models.TextField()
    slug = models.SlugField()
    objects = models.Manager()
    def __str__(self):
        return self.name
 
    def get_absolute_url(self): 
        return reverse('umk:institute_detail', args=[str(self.id)])

class Department(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    info = models.TextField()
    institute = models.ForeignKey(Institute, on_delete = models.CASCADE)

class Employee(models.Model):
    POSITION_CHOICES = (
        ('сотрудник', 'Сотрудник'),
        ('заведующий', 'Заведующий'),
    )
    position = models.CharField(max_length=30, choices=POSITION_CHOICES)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Document(models.Model):
    DOC_CHOICES = (
        ('фгос', 'ФГОС'),
        ('учебный план', 'Учебный план'),
        ('рпд','РПД')
    )
    doc_type = models.CharField(max_length=30, choices=DOC_CHOICES)
    document = models.FileField(upload_to='documents/',null=True)
    def filename(self):
        return os.path.basename(self.document.name)

class Direction(models.Model):
    QUALIFICATION_CHOICES = (
        ('бакалавр', 'Бакалавр'),
        ('магистр', 'Магистр'),
        ('специалист','Специалист'),
    )
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=8)
    slug = models.SlugField(max_length=200, unique=True)   
    qualification = models.CharField(max_length=50,choices=QUALIFICATION_CHOICES)
    standart_period = models.PositiveIntegerField()
    fgos = models.ForeignKey(Document,on_delete=models.PROTECT)
    institute = models.ForeignKey(Institute,on_delete=models.CASCADE)
    objects = models.Manager()
    def __str__(self):
        return self.name
 
    def get_absolute_url(self): 
        return reverse('umk:direction_detail', args=[str(self.id)])

class StudentGroup(models.Model):
    name = models.CharField(max_length=250)
    start_year = models.PositiveIntegerField(
            validators=[
                MinValueValidator(2010), 
                MaxValueValidator(datetime.now().year+5)],
            help_text="Используйте формат: <YYYY>")
    TYPE_CHOICES=(
        ('очная','очная'),
        ('очно-заочная','очно-заочная'),
        ('заочная','заочная')
        )
    form = models.CharField(max_length=50, choices=TYPE_CHOICES)
    n_semesters = models.PositiveIntegerField()
    #uch_plane = models.ForeignKey(Document,on_delete=models.PROTECT)
    direction = models.ForeignKey(Direction,on_delete=models.PROTECT)



class Discipline(models.Model):
    IC_CHOICES = (
        ('зачет', 'Зачет'),
        ('экзамен', 'Экзамен'),
    )
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200, unique=True)
    purpose = models.TextField()
    task = models.TextField()
    credits = models.PositiveIntegerField()
    lectures = models.PositiveIntegerField()
    workshops = models.PositiveIntegerField()
    independent = models.PositiveIntegerField()
    intermediate_certification = models.CharField(max_length=50,choices=IC_CHOICES)
    direction = models.ForeignKey(Direction,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

class Section(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=250)
    discipline = models.ForeignKey(Discipline,on_delete = models.CASCADE)

class Theme(models.Model):
    LESSON_CHOICES = (
        ('сотрудник', 'Сотрудник'),
        ('заведующий', 'Заведующий'),
    )
    number = models.PositiveIntegerField()
    lesson_type = models.CharField(max_length=30,choices=LESSON_CHOICES)
    labor_intensity = models.PositiveIntegerField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)



    


