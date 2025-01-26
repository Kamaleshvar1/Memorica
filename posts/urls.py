from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('feed/', views.feed, name='feed'),
    path('like/', views.like_post, name='like'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)