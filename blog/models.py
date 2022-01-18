from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField


# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
#
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'
#
#     def __str__(self):
#         return self.name


# class Blog(models.Model):
#     title = models.CharField(max_length=255)
#     # category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
#     photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
#     # author = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = []
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['-created_at']
#
#     def __str__(self):
#         return self.title


# class Comment(models.Model):
#     post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
#     author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = 'Comment'
#         verbose_name_plural = 'Comments'
#
#     def __str__(self):
#         return "%s - %s" % (self.post.title, self.author.username)
