from django.db import models

class Room(models.Model):
    password = models.CharField(max_length=255)
    talk_id = models.CharField(max_length=255)
    user1_uid = models.CharField(max_length=255)
    user1_provider = models.CharField(max_length=255)
    user2_uid = models.CharField(null=True, max_length=255)
    user2_provider = models.CharField(null=True, max_length=255)
    created_at = models.IntegerField()
    updated_at = models.IntegerField()
    is_close = models.BooleanField(default=False)
    is_wait = models.BooleanField(default=True)
    flag = models.IntegerField(default=0)