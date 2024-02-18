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
from home.views import home_view, calculation_view
from post.views import post_list_view, post_create_view, post_detail_view, post_edit_view, post_delete_view
 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('calculation/', calculation_view, name="calculation"),
    path('post/list/', post_list_view, name= "post-list"),
    path('post/create/', post_create_view, name= "post-create"),
    path("post/<int:id>/detail/", post_detail_view, name="post-detail"),
    path("post/<int:id>/edit/", post_edit_view, name="post-edit"),
    path("post/<int:id>/delete/", post_delete_view, name="post-delete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
