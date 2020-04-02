from django.urls import path, re_path
from . import views
from django.views.generic.base import TemplateView

# django 2.0 버전부터는 url 대신 path, re_path(정규식)만 사용
urlpatterns = [
    # 첫 번째 인수는 일치시킬 경로(패턴), 두 번째 인수는 패턴이 일치할때 호출되는 다른 함수(views.py 파일에 존재)
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # 고급 경로 매칭/정규 발현 프라이머
    re_path(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    path('jsgrid/',TemplateView.as_view(template_name='jsgrid.html')),
]