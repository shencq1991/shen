from django.db import models
from django.urls import reverse
from  datetime  import  *
import  time

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    industry = models.TextField()
    province = models.CharField(max_length=20)
    created_date = models.TextField()
    address = models.TextField()
    author = models.CharField(max_length=20,default="wm-station")
    update_time = models.DateTimeField(default=datetime.now)
    date = models.TextField()
    net_profits = models.TextField()
    esp = models.TextField()
    business_income = models.TextField()
    bips = models.TextField()
    Asset = models.TextField()
    scale = models.TextField()
    roe_yoy = models.TextField()
    esp_yoy = models.TextField()
    bvps = models.TextField()
    epcf = models.TextField()
    profits_yoy = models.TextField()
    roe = models.TextField()
    net_profit_ratio = models.TextField()
    gross_profit_rate = models.TextField()
    arturnover = models.TextField()
    inventory_turnover = models.TextField()
    currentasset_turnover = models.TextField()
    business_income_yoy = models.TextField()
    nav = models.TextField()
    targ = models.TextField()
    epsg = models.TextField()
    currentratio = models.TextField()
    quickratio = models.TextField()
    cashratio = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content', kwargs={'pk': self.pk})


class Post300(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    industry = models.TextField()
    province = models.CharField(max_length=20)
    created_date = models.TextField()
    address = models.TextField()
    author = models.CharField(max_length=20,default="wm-station")
    update_time = models.DateTimeField(default=datetime.now)
    date = models.TextField()
    net_profits = models.TextField()
    esp = models.TextField()
    business_income = models.TextField()
    bips = models.TextField()
    Asset = models.TextField()
    scale = models.TextField()
    roe_yoy = models.TextField()
    esp_yoy = models.TextField()
    bvps = models.TextField()
    epcf = models.TextField()
    profits_yoy = models.TextField()
    roe = models.TextField()
    net_profit_ratio = models.TextField()
    gross_profit_rate = models.TextField()
    arturnover = models.TextField()
    inventory_turnover = models.TextField()
    currentasset_turnover = models.TextField()
    business_income_yoy = models.TextField()
    nav = models.TextField()
    targ = models.TextField()
    epsg = models.TextField()
    currentratio = models.TextField()
    quickratio = models.TextField()
    cashratio = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content300', kwargs={'pk': self.pk})


class Echarts(models.Model):
    Xb = models.CharField(max_length=20)
    num = models.CharField(max_length=20)









