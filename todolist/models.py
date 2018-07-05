from django.db import models

# Create your models here.
class Todo(models.Model):
    events = models.CharField(max_length=50)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.events