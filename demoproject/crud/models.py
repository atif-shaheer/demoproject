from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class slider(models.Model):
    heading = models.CharField(max_length=50)
    paragraph = models.CharField(max_length=50)
    slide = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.heading