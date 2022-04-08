from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return super().__str__()