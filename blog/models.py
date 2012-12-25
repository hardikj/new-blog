from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=500)
    content=models.TextField()
    date=models.DateField()

    def __unicode__(self):
        return self.title
 
