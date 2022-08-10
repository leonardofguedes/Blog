from django.urls import path
from .views import PostListView, post_detail

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='detail')
]
