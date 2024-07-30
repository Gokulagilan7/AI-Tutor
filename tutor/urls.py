from django.urls import path
from . import views

urlpatterns = [
    path('recommendations/<int:user_id>/', views.recommend_lessons, name='recommendations'),
    # path('', views.recommend_lessons(), name=''),
]
