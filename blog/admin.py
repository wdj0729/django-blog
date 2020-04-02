from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)

#Register the admin class with the associated model
@ admin.register(Post)

# Define the admin class
class PostAdmin(admin.ModelAdmin):
    # 목록보기 구성
    list_display = ('author', 'title', 'text', 'created_date', 'published_date')
    # 목록 필터 추가
    list_filter = ('author', 'created_date', 'published_date')
    # 세부 사항보기 섹션
    fieldsets = (
        (None, {
            'fields': ('author', 'title', 'text')
        }),
        ('Date', {
            'fields' : ('created_date', 'published_date')
        }),
    )

#Register the admin class with the associated model
@ admin.register(Comment)

# Define the admin class
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'text', 'created_date', 'approved_comment')
    list_filter = ('author', 'created_date', 'approved_comment')
    # 표시 및 배치 할 필드 제어
    fields = [
        'author', 'created_date', 'approved_comment'
    ]

