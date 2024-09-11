from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'teste1'),
    (1, 'teste2')
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    teste = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
