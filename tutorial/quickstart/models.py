from django.db import models

class File(models.Model):
    name = models.TextField(blank=False, null=False)
    data = models.TextField(blank=False, null=False)


