from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=20)
    adr = models.CharField(max_length=50)

    create_day = models.DateTimeField(auto_now_add=True)
    update_day = models.DateTimeField(auto_now=True)