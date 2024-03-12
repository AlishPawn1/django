from django.db import models
from accounts.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField("Post title", max_length= 100)
    content = models.TextField("Post Content")
    image = models.ImageField("Post Image", upload_to="post", default="its_me.jpg")
    
    no_of_views = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self) -> str:
        return self.title