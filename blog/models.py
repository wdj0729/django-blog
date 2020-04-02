from django.conf import settings
from django.db import models
from django.utils import timezone
# pylint: disable=E1101

class Post(models.Model):
    # 다른 테이터베이스 모델과 일대 다 관계를 지정
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 중간에서 중간 크기의 고정 길이 문자열 정의
    title = models.CharField(max_length=50, help_text='Enter the title')
    # 임의 길이의 큰 문자열
    text = models.TextField()
    # 날짜 및 날짜/시간 정보를 저장/표시
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text