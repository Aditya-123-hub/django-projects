from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostCreateForm,CommentForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.http import JsonResponse

# Create your views here.

@login_required
def post_create(request):
    if request.method=='POST':
        form=PostCreateForm(data=request.POST, files=request.FILES)  
        if form.is_valid():
            post=form.save(commit=False) #abhi save mtt kr
            post.user=request.user
            post.save()
            return redirect('feed')
            
    else:
        form=PostCreateForm(data=request.GET)
    return render(request,'posts/create.html',{'form':form}) 

@login_required
def feed(request):
    posts = Post.objects.all()
    logged_user = request.user
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():   # ✅ safety check
            new_comment = comment_form.save(commit=False)
            post_id = request.POST.get("post_id")
            post = get_object_or_404(Post, id=post_id)
            new_comment.post = post
            new_comment.save()
            # ✅ Redirect to avoid re-posting on refresh
            return redirect("feed")  

    context = {
        "comment_form": comment_form,
        "posts": posts,
        "logged_user": logged_user,
    }
    return render(request, "posts/feed.html", context)


def like_post(request):
    post_id = request.POST.get('post_id')
    post=get_object_or_404(Post,id=post_id)
    if post.liked_by.filter(id=request.user.id.exist()):
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)  
        return redirect('feed')  



