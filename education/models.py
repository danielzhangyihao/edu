from django.db import models

# Create your models here.
class Lesson(models.Model):
    lesson_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    description = models.CharField(max_length=800)
    is_completed = models.BooleanField(default=False)
    price = models.IntegerField()
    lesson_schedule = models.CharField(max_length=800)
    subject = models.CharField(max_length=200)

class Instructor(models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    description = models.CharField(max_length=800)
    lessons = models.ManyToManyField(Lesson)
