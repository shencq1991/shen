from django.db import models
from django.urls import reverse
from  datetime  import  *
import  time

# Create your models here.

# class Post(models.Model):
#     name = models.CharField(max_length=20)
#     code = models.CharField(max_length=20)
#     author = models.CharField(max_length=20,default="wm-station")
#     created_time = models.DateTimeField(default=datetime.now)
#     industry = models.TextField()
#     area = models.TextField()
#     pe = models.TextField()
#     outstanding = models.TextField()
#     totals = models.TextField()
#     totalAssets = models.TextField()
#     liquidAssets = models.TextField()
#     fixedAssets = models.TextField()
#     reserved = models.TextField()
#     reservedPerShare = models.TextField()
#     pb = models.TextField()
#
#     date = models.TextField()
#     roe = models.TextField()
#     esp = models.TextField()
#     net_profits = models.TextField()
#     business_income = models.TextField()
#     net_profit_ratio = models.TextField()
#     gross_profit_rate = models.TextField()
#     arturnover = models.TextField()
#     inventory_turnover = models.TextField()
#     currentasset_turnover = models.TextField()
#     mbrg = models.TextField()
#     nprg = models.TextField()
#     nav = models.TextField()
#     targ = models.TextField()
#     epsg = models.TextField()
#     currentratio = models.TextField()
#     quickratio = models.TextField()
#     cashratio = models.TextField()
#     cf_sales = models.TextField()
#     rateofreturn = models.TextField()
#     cf_nm = models.TextField()
#     cf_liabilities = models.TextField()
#     cashflowratio = models.TextField()
#     epcf = models.TextField(default="wm-station")
#     bvps = models.TextField(default="wm-station")
#     bips = models.TextField()
#
#
#
#
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('content', kwargs={'pk': self.pk})
#
# class Echarts(models.Model):
#     Xb = models.CharField(max_length=20)
#     num = models.CharField(max_length=20)








