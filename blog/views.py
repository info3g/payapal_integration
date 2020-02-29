from .models import Post
from django.views import generic
from django.shortcuts import render

class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    model = Post
    template_name = 'blog/blog_index.html'
    paginate_by = 6


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/blog_post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['other_posts'] = Post.objects.filter(status=1).order_by('-created_on')[:3]
        return context
