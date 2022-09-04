from pyexpat import model
from django.db import models

# Create your models here.
class BlogDetails(models.Model):
    blog_name = models.CharField(max_length=100, default='N/A')
    time_of_creation = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, default='admin')

class BlogContent(models.Model):
    blog = models.OneToOneField(BlogDetails, on_delete=models.CASCADE, primary_key=True)
    blog_content = models.TextField(default='N/A')