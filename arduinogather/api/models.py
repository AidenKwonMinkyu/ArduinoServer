from django.db import models

# Create your models here.

class TimeStampMixin(models.Model):
    admin_memo = models.TextField(blank=True, null=False, verbose_name='Admin Memo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class GatherItem(TimeStampMixin):
    mac = models.TextField(blank=True,null=False)
    temperature = models.FloatField(blank=True,null=False)
    humidity = models.FloatField(blank=True,null=False)
    bmpTemperature = models.FloatField(blank=True,null=False)
    bmpPressure = models.FloatField(blank=True,null=False)
    bmpAltitude = models.FloatField(blank=True,null=False)
    concentration = models.FloatField(blank=True,null=False)
    ugm3 = models.FloatField(blank=True,null=False)


