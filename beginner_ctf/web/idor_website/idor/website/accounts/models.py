from django.db import models
import random

def random_string():
    return str(random.randint(10, 99))

class Note(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    note_id = models.CharField(max_length=10, default = random_string())

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

