from django.db import models

class Courses(models.Model):
    name = models.TextField()
    text = models.TextField()

class News(models.Model):
    name = models.TextField()
    text = models.TextField()
    date = models.DateTimeField()

class Teachers(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    patronymic = models.TextField()
    description = models.TextField()
    birthday = models.DateField()