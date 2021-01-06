from django.shortcuts import get_object_or_404, render
from .models import Post, Comment
from .forms import NewComment

def home(request):
    context = {
        'title':'الصفحة الرئيسية',
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)
def about(request):
    context = {
        'title':'من انا',
    }
    return render(request, 'blog/about.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    comment_form = NewComment()
    context = {
        'title':post.title,
        'post':post,
        'comments':comments,
        'comment_form':comment_form
    }
    return render(request, 'blog/detail.html', context)