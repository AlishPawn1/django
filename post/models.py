from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField("Post title", max_length= 100)
    content = models.TextField("Post Content")
    image = models.ImageField("Posst Image", upload_to="post", default="its_me.jpg")
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)

    def __str__(self) -> str:
        return self.title