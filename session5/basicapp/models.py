from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    port_folio_site = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profle_pics', blank=True)

    def __str__(self):
        return self.user.username

