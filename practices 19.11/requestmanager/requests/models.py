from django.db import models


class Request(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.TextField(max_length=200)
    submitted_at = models.DateTimeField(auto_now_add=True)



