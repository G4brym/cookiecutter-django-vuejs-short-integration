from django.db import models


class Timestamped(models.Model):
    class Meta:
        abstract = True
        ordering = ["-pk"]

    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
