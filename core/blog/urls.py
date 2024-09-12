from django.urls import path, include
from . import views

app_name="blog"

urlpatterns = [
    path('', views.TestViwe.as_view()),
    path('posts/', views.PostListViwe.as_view(),name='posts_list'),
    path('singel-post/<int:pk>/', views.PostDetailView.as_view(),name='post-detail'),
    path('create/', views.PostCreateView.as_view(),name='create-post'),
    path('api/v1/',include('blog.api.v1.urls'))
]