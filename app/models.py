from django.db import models

# Create your models here.

class Topic(models.Model):
    S_No=models.IntegerField()
    Topic_Name=models.CharField(max_length=30, primary_key=True)

    def __str__(self) -> str:
        return self.Topic_Name


class Webpage(models.Model):
    S_No=models.IntegerField(primary_key=True)
    Topic_Name=models.ForeignKey(Topic, on_delete=models.CASCADE)
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    url=models.URLField()

    def __str__(self) -> str:
        return self.Name
    
class AccessRecord(models.Model):
    Name=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    Author=models.CharField(max_length=30)
    date=models.DateField()

    def __str__(self) -> str:
        return self.author
