from django.db import models


class Courses(models.Model):
    name = models.TextField()
    text = models.TextField()

    def __str__(self):
        return f"{self.name}"


class News(models.Model):
    name = models.TextField()
    text = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"


class Teachers(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    patronymic = models.TextField()
    description = models.TextField()
    birthday = models.DateField()
    photo = models.ImageField(upload_to='img')

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"
