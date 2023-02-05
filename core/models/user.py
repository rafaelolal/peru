
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(User):
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse(f"core:user_detail", kwargs={"pk": self.pk})