import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Puzzle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    intro = models.TextField('Introduction', blank=True)
    description = models.TextField('Description', blank=True)
    question = models.TextField('Question', blank=True)
    explanation = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='puzzles/', blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL, related_name='puzzles')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('puzzle_detail', args=[str(self.id)])

    def get_correct_choices(self):
        return self.choices.filter(is_correct=True)


class Choice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return self.text

    def is_correct(self):
        return self.is_correct
