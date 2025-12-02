from django.db import models

# Create your models here.
class Bank(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=49)
    class Meta:
        db_table = 'banks'
class Branch(models.Model):
    ifsc = models.CharField(max_length=11,primary_key=True)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE,related_name="bank",db_column="bank_id")
    branch_name = models.CharField(max_length=74,db_column="branch")
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    class Meta:
        db_table = 'branches'