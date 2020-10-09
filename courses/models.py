import uuid

from django.db import models
from django.urls import reverse


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    cover = models.ImageField(upload_to='covers/')

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])
