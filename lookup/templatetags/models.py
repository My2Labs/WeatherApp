from django.db import models

class Item(models.Model):
    item = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.item