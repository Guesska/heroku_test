from django.db import models

# Create your models here.


class AboutMe(models.Model):
    image = models.ImageField(upload_to='images/about_me/%Y/%m/%d/', blank=True, verbose_name='Изображение')