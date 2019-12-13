from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.urls import reverse


class transactions(models.Model):
    email = models.CharField(max_length=255)
    pwned = models.CharField(max_length=255)
    breaches =ArrayField(
        models.CharField(max_length= 255, blank=True)
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('deleterecord', kwargs={'pk': self.pk})