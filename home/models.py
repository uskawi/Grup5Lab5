from django.db import models


class Img(models.Model):
    """Car model"""
    name = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)



    def __str__(self):
        return str(self.name)
