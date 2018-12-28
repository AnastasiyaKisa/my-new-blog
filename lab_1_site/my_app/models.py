from django.db import models
from django.utils import timezone
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
def publish(self):
    self.save()

class PostPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    task_status=models.BooleanField(default=False)
