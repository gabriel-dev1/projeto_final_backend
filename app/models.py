from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    content = models.TextField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='post')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
