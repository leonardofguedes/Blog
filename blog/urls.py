from django.urls import path
from .views import post_list, post_detail

urlpatterns = [
    path('/', post_list, name='list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='detail')
]
