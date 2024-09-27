from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30) #30자 이하
    content = models.TextField() #문자열 길이를 정의하지 않는 긴 문자열
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)