
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class StockAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=100)
    stock_symbol = models.CharField(max_length=20)
    analysis_report = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stock_name 
