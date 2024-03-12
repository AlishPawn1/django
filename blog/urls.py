"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from accounts.views import login_view, register_view

from home.views import home_view, calculation_view, contact_view
from post.views import post_list_view, post_create_view, post_detail_view, post_edit_view, post_delete_view, PostCreateView, PostDeleteView, PostDetailView, PostEditView, PostListView, UserPostListView
from profiles.views import profile_create_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', login_view, name = "login" ),
    path('accounts/register/', register_view, name = "register" ),
    path('accounts/logout/', LogoutView.as_view(), name = "logout" ),
    # path('', home_view, name="home"),
    path('calculation/', calculation_view, name="calculation"),
    # method call
    # path('post/list/', post_list_view, name= "post-list"),
    # path('post/create/', post_create_view, name= "post-create"),
    # path("post/<int:id>/detail/", post_detail_view, name="post-detail"),
    # path("post/<int:id>/edit/", post_edit_view, name="post-edit"),
    # path("post/<int:id>/delete/", post_delete_view, name="post-delete"),
    # path("profile/create/", profile_create_view, name= 'profile-create'),
    
    # class call
    path('user/post/list/', UserPostListView.as_view(), name= "user-post-list"),
    path('', PostListView.as_view(), name= "home"),
    path('post/create/', PostCreateView.as_view(), name= "post-create"),
    path("post/<int:id>/detail/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:id>/edit/", PostEditView.as_view(), name="post-edit"),
    path("post/<int:id>/delete/", PostDeleteView.as_view(), name="post-delete"),

    
    path("contact/", contact_view, name= "contact"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
