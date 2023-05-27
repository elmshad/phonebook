from django.db import models
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contacts:contact_details', args=[self.pk])


class Number(models.Model):
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, related_name='numbers')
    number = models.CharField(max_length=200)

    def __str__(self):
        return self.number
