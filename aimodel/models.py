from django.db import models
#ORM takes places here 
class cardata(models.Model):
    onroad_price = models.IntegerField()
    year = models.IntegerField()
    km = models.IntegerField()
    condition = models.IntegerField()
    economy = models.IntegerField()
    model_prediction = models.FloatField()
