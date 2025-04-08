from django.db import models

class Cabinet(models.Model):
    name = models.CharField(max_length=100)
    requires_questions = models.BooleanField(default=False)

class Question(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, related_name="questions")
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title