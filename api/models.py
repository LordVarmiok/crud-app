from django.db import models
from django.contrib.auth.models import User
import uuid


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120, unique=False)
    text = models.TextField(blank=False)
    date_added = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.get_author_username()}'

    def get_author_username(self):
        return self.author.username


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField(blank=False)
    date_added = models.DateField(auto_now_add=True)
    note_origin = models.ForeignKey(Note, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.id}'