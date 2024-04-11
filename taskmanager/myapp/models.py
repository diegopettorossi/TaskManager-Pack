from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    def __str__(self):
        return self.title
