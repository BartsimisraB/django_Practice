from django.db import models


class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    create_day = models.DateTimeField(auto_now_add=True)
    update_day = models.DateTimeField(auto_now=True)
