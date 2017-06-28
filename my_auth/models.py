from django.db import models
from django.contrib.auth.models import User


class UserProfileImage(models.Model):
    image = models.ImageField(upload_to='image/%Y/%m/', max_length=255,
                              height_field='height_field',
                              width_field='width_field')
    height_field = models.PositiveSmallIntegerField()
    width_field = models.PositiveSmallIntegerField()

    def get_absolute_url(self, size=None):
        return '/%s/' % self.image.url

class UserProfile(User):
    image = models.OneToOneField(UserProfileImage, blank=True, null=True)
    address = models.TextField(blank=True)
