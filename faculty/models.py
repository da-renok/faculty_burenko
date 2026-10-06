from django.db import models
from django.utils import timezone

class HomePage(models.Model):

    title = models.CharField(max_length=200)
    text = models.TextField()
    contacts = models.TextField()

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=200)
    coordinator_contact = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,related_name='programs')
    subjects = models.TextField(help_text='Кожна дисципліна з нового рядка')

    def subject_list(self):
        return [s for s in self.subjects.splitlines() if s.strip()]

    def __str__(self):
        return f'{self.code} {self.name}'


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name='teachers')

class ExchangeProgram(models.Model):
    university = models.CharField(max_length=255)
    country = models.CharField(max_length=100, default='')
    languages = models.CharField(max_length=255)
    seats = models.PositiveIntegerField()
    deadline = models.DateField()
    description = models.TextField()

    @property
    def is_open(self):
        return self.deadline >= timezone.localdate()
    def __str__(self):
        return self.university
