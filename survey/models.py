from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Poll(models.Model):
    prompt = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.prompt


class Response(models.Model):
    question = models.ForeignKey(Poll)
    answer = models.CharField(max_length=256)

    def __unicode__(self):
        return self.answer

