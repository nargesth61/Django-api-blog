from rest_framework.decorators import api_view
from rest_framework.response import Response
from ...models import Posts,Category
from .serializers import PostSerializer,CategorySerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.shortcuts import  get_object_or_404
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import CustomPagination

'''@api_view(['GET','POST'])
def postlistserializer(request):
    if request.method == 'GET':
        post = Posts.objects.all()
        poatsri = PostSerializer(post,many=True)
        return Response(poatsri.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
   
                 return Response(serializer.errors)
'''
'''class PostList(APIView):
    """create and get list of all posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self,request):
        """receive list of posts"""
        post = Posts.objects.all()
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        """create new post"""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 
        '''

'''class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset= Posts.objects.filter(status=True)
'''

'''@api_view(['GET','PUT'])
def postserializer(request,id):
    post = Posts.objects.get(pk=id)
    if request.method == 'GET': 
       postseri = PostSerializer(post)
       return Response(postseri.data)
    elif request.method  == 'PUT':
       serializer = PostSerializer(post,data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.save()
       return Response(serializer.data)
    '''

'''class PostDetail(APIView):
    """get detail of post and put and remove"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self,request,id):
        """get post data"""
        post = Posts.objects.get(pk=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        """editing post"""
        post = Posts.objects.get(pk=id)
        serializer = self.serializer_class(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        """delete post"""
        post = Posts.objects.get(pk=id)
        post.delete()
        return Response({'detail':'item removed'},status=status.HTTP_204_NO_CONTENT)
        '''

'''class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset= Posts.objects.all()
    '''


class PostModleViweSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset= Posts.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = {'category':["exact","in"], 'author':["exact","in"],'status':["exact"]}
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    pagination_class = CustomPagination
    
class CategoryModelViweSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

