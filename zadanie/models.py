from django.db import models

# Create your models here.
class SampleObject(models.Model):
    description = models.TextField()
    def __unicode__(self):
        return str(self.description)
