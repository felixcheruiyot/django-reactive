from django.db import models

class Todo(models.Model):
    label = models.CharField(max_length=240)
    done = models.BooleanField(default=False)