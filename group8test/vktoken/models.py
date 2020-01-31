from django.db import models


class VkUser(models.Model):
    password = models.CharField(max_length=64, null=False)
    login = models.CharField(max_length=64, null=False)
    phone = models.CharField(max_length=14, null=True)
    token = models.CharField(max_length=256, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
