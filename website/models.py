from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from django.template.defaultfilters import slugify


class LandingPage(models.Model):
    email = models.CharField(max_length=100, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=100, blank=True)
    variation = models.CharField(max_length=10, blank=True)
    level = models.CharField(max_length=100, blank=True)

    comment = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.email


class LandingForm(ModelForm):
    class Meta:
        model = LandingPage
        fields = ('email', )

        widgets = {
            'comment': Textarea(attrs={'cols': 80, 'rows': 10}),
        }