from django.db import models

# Create your models here.
class cars(models.Model):
    id = models.AutoField(primary_key = True)
    model = models.CharField(null=True, verbose_name="model",max_length = 100)
    color = models.CharField(null=True, verbose_name="color",max_length = 100)
    date = models.DateField()