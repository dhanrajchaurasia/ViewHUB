from django.db import models

# Create your models here.
class chat(models.Model):
    room_name = models.CharField(max_length=255)
    allowed_user = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name