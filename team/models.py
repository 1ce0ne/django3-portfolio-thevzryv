from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=200)
    age = models.SmallIntegerField()
    description = models.TextField()
    specialty = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='team/images/')
    

    def __str__(self):
        return self.name