from django.urls import path
from blog.views.post_list_view import *
from blog.views.detail_view import *
from blog.views.post_share_view import *


urlpatterns = [
    path('', post_list, name='list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag')
]
