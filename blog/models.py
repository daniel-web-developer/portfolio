from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(null=True, max_length=100)
    content = models.TextField(null=True)
    pub_date = models.DateTimeField(timezone.now(), auto_now_add=True)
    edit_date = models.DateTimeField(null=True)
    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f"{self.id}: Title: {self.title}, Content: {self.content} | Date published: {self.pub_date} | Date edited: {self.edit_date}"