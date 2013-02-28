from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.template.defaultfilters import slugify


class LandingPage(models.Model):
    email = models.CharField(max_length=100, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=100, blank=True) #IPAddressField()
    variation = models.CharField(max_length=10, blank=True)
    comment = models.CharField(max_length=500, blank=True)

    def __unicode__(self):
        return self.email


class LandingForm(ModelForm):
    class Meta:
        model = LandingPage
        fields = ('email',)
