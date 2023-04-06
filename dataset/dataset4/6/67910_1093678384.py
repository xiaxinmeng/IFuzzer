from django.db import models

class Model(models.Model):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)