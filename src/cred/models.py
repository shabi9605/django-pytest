from django.db import models
from django.utils import timezone

# Create your models here.


class Cred(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(db_index=True, default=timezone.now)

    def __str__(self):
        return str(self.id)