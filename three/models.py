from django.db import models

class Food(models.Model):
    name=models.CharField(max_length=20)
    adr=models.CharField(max_length=50)
    pw=models.CharField(max_length=20,default=None,null=True)

    create_day=models.DateTimeField(auto_now_add=True)
    update_day=models.DateTimeField(auto_now=True)

class Review(models.Model):
    score=models.IntegerField()
    comment=models.CharField(max_length=100)

    res=models.ForeignKey(Food,on_delete=models.CASCADE)
    create_day = models.DateTimeField(auto_now_add=True)
    update_day = models.DateTimeField(auto_now=True)






