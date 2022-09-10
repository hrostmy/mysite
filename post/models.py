from django.db import models

# Create your models here.

class Post(models.Model):
    photo = models.ImageField('Add photo:', blank=True)
    text = models.CharField('Add text:', max_length=1000)
    date = models.DateTimeField('Date', auto_now_add=True, blank=True)

    def __str__(self):
        return 'id: '+str(self.pk)+' date: '+str(self.date)