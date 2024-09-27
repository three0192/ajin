from django.db import models

class Restaurant(models.Model): # Restaurant 라는 상점을 나타내는 모델을 정의
    name = models.CharField(max_length=30)  # 이름
    address = models.CharField(max_length=200)  # 주소

    created_at = models.DateTimeField(auto_now_add=True)  # 글 작성 시 (이 모델의 데이터(레코드) 저장 시) 생성 시각
    updated_at = models.DateTimeField(auto_now=True)  # 저장된 레코드 수정 시 수정 시각
