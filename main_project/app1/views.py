from django.shortcuts import render
from models import BlogDetails, BlogContent


# Create your views here.
def BlogPage(request, blog_name):
    blog_instance = BlogDetails.objects.filter(blog_name=blog_name)[0]
    blog_content_value = BlogContent.objects.filter(blog=blog_instance)[0].blog_content
    blog_created_on = blog_instance..strftime("%d/%m/%Y, %H:%M")
    blog_created_by = blog_instance.created_by