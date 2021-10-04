from django.contrib.auth import get_user_model
from django.db import models

from images.validators import validate_file_type


class Image(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='images')
    name = models.CharField(max_length=100)
    url = models.FileField(upload_to='images/', validators=[validate_file_type])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
