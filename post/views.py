from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class UserPostListView(LoginRequiredMixin, View):
    # pass
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(user = request.user)
        return render(request, "profile/posts.html", {"posts": posts})

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        print("posts: ", posts)
        return render(
            request, 
            "post/list.html",
            context={"posts": posts},
        )

def post_list_view(request):
    posts = Post.objects.all()
    print("Posts: ", posts)
    return render(request, "post/list.html", context={"posts": posts},)

from post.forms import PostCustomForm



class PostCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostCustomForm
        return render(request, "post/create.html", {"form": form})
    
    def post(self, request, *args, **kwargs):
        print("request post data", request.POST, request.FILES)
        form = PostCustomForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            post = Post.objects.create(
                title = form.cleaned_data.get('title'), 
                content = form.cleaned_data.get('content'), 
                image = form.cleaned_data.get('image'), 
                user = request.user
            )
            return redirect('post-list')
        return render(request, "post/create.html", {"form": form})
@login_required
def post_create_view(request):
    if request.method == "GET":
        form = PostCustomForm
        return render(request, "post/create.html", {"form": form})
    else:
        print("request post data", request.POST, request.FILES)
        form = PostCustomForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            post = Post.objects.create(
                title = form.cleaned_data.get('title'), 
                content = form.cleaned_data.get('content'), 
                image = form.cleaned_data.get('image'), 
                user = request.user
            )
            return redirect('post-list')
        return render(request, "post/create.html", {"form": form})


class PostDetailView(View):
    def get(self, request, id, *args, **kwargs):
        try:
            post = Post.objects.get(id = id)
            post.no_of_views = post.no_of_views + 1
            post.save()
            return render(request, "post/details.html",{"post":post})
        except Exception as e:
            return render(request, "errors/404.html")   

def post_detail_view(request, id):
    try:
        post = Post.objects.get(id= id)
        return render(request, "post/details.html",{"post":post})
    except Exception as e:
        return render(request, "errors/404.html")

from post.forms import PostModelForm



class PostEditView(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            post = Post.objects.get(id=id, user = request.user)
        except Exception as e:
            return render(request, "errors/404.html")
        else: 
            form = PostModelForm(instance=post)
            return render(request, "post/edit.html",
                          {
                        "form": form,
                    })
    def post(self, request, id, *args, **kwargs):
        try:
            post = Post.objects.get(id=id, user = request.user)
        except Exception as e:
            return render(request, "errors/404.html")
        else: 
            form = PostModelForm(
                instance = post,
                data=request.POST,
                files=request.FILES,
            )
            if form.is_valid():
                form.save()
                return redirect("post-list")
            else:
                return render(
                    request, "post/edit.html",
                    {
                        "form": form,
                    }
                )
            
@login_required        
def post_edit_view(request, id):
    try:
        post = Post.objects.get(id=id, user = request.user)
    except Exception as e:
        return render(request, "errors/404.html")
    else:
        if request.method == "GET":
            form = PostModelForm(instance=post)
            return render(request, "post/edit.html",
                          {
                        "form": form,
                    })
        else:
            form = PostModelForm(
                instance = post,
                data=request.POST,
                files=request.FILES,
            )
            if form.is_valid():
                form.save()
                return redirect("post-list")
            else:
                return render(
                    request, "post/edit.html",
                    {
                        "form": form,
                    }
                )
                


class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        try:
            post = Post.objects.get(id=id, user = request.user)
            post.delete()
            return redirect("post-list")
        except Exception as e:
            return render(request, "errors/404.html")
@login_required
def post_delete_view(request, id):
    try:
        post = Post.objects.get(id=id, user = request.user)
        post.delete()
        return redirect("post-list")
    except Exception as e:
        return render(request, "errors/404.html")