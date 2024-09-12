
from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DeleteView,CreateView
from .models import *

# Create your views here.

class TestViwe(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'narges'
        return context


class PostListViwe(ListView):
    '''
    show list of post whit cbv
    '''
    queryset = Posts.objects.all()
    context_object_name = 'posts'
    paginate_by = 2
    ordering = '-id'

'''
 show details of posts in the page
'''
class PostDetailView(DeleteView):
    model = Posts
    template_name = 'blog/single-post.html'

class PostCreateView(CreateView):
    model =Posts
    fields = ['title','content','status','category','published_date']
    success_url = '/blog/posts/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)