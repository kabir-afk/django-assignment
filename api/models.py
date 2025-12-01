from django.db import models

# Create your models here.
class Bank(models.Model):
    id = models.BigIntegerField(primary_key=True , null=False)
    name = models.CharField(max_length=49)
    class Meta:
        db_table = 'banks'
class Branch(models.Model):
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE,related_name="branch")
    ifsc = models.CharField(max_length=11,null=False)
    name = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    class Meta:
        db_table = 'branches'