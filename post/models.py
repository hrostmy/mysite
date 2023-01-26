from django.db import models
# Create your models here.
from django.urls import reverse

from accounts.models import User


class Post(models.Model):
    photo = models.ImageField('Add photo:', blank=True)
    text = models.CharField('Add text:', max_length=1000)
    date = models.DateTimeField('Date', auto_now_add=True, blank=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return 'id: ' + str(self.pk) + ' date: ' + str(self.date)

    def get_absolute_url(self):
        return reverse('post_detail', args=(self.pk,))
