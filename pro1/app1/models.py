from django.db import models


class Coffee(models.Model):
    name = models.CharField(max_length=20, null=True)
    amount = models.CharField(max_length=10, null=True, default=None)
    payment_id = models.CharField(max_length=100,null=True)
    paid = models.BooleanField(default=False)

