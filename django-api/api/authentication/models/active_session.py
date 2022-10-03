from django.db import models


class ActiveSession(models.Model):
    user = models.ForeignKey("api_user.User", on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
