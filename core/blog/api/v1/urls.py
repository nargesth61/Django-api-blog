from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name="api"
router = DefaultRouter()
router.register('post', views.PostModleViweSet,basename='post')
router.register('category', views.CategoryModelViweSet,basename='category')
urlpatterns =router.urls

#urlpatterns = [
    #path('post/<int:id>/', views.postserializer,name='post'),
    # path('posts/', views.postlistserializer,name='post'),
    #path('posts/', views.PostList.as_view(),name='post'),
    #path('post/<int:pk>/', views.PostDetail.as_view(),name='post-detail'),
    #path('posts/', views.PostViweSet.as_view({'get':'list','post':'create'}),name='post'),
    #path('post/<int:pk>/', views.PostViweSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}),name='post-detail'),
#]