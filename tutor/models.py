from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

class UserLessonInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    rating = models.IntegerField()

