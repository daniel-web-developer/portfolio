from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(null=True, max_length=100)
    screens = models.ImageField(upload_to="static/projects")
    pub_date = models.DateTimeField(timezone.now(), auto_now_add=True)
    gitlink = models.URLField()

    class Meta:
        ordering = ['-pub_date']