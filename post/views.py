from django.shortcuts import render, redirect
from post.models import Post

# Create your views here.
def post_list_view(request):
    posts = Post.objects.all()
    print("Posts: ", posts)
    return render(request, "post/list.html", context={"posts": posts},)

from post.forms import PostCustomForm
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
            )
            return redirect('post-list')
        return render(request, "post/create.html", {"form": form})

def post_detail_view(request, id):
    try:
        post = Post.objects.get(id= id)
        return render(request, "post/details.html",{"post":post})
    except Exception as e:
        return render(request, "errors/404.html")

from post.forms import PostModelForm
def post_edit_view(request, id):
    try:
        post = Post.objects.get(id=id)
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
                
def post_delete_view(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return redirect("post-list")
    except Exception as e:
        return render(request, "errors/404.html")