from django.db import models
from accounts.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField("First Name", max_length=100, null=True, blank=True)
    last_name = models.CharField("Last Name", max_length=100, null=True, blank=True)
    email = models.EmailField("Email", max_length=100, null=True, blank=True)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="profiles")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
