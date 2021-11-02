from django.db import models

# Create your models here.
class CompanyList(models.Model):
    cmp_name = models.CharField(max_length=100)
    cmp_inderstry = models.CharField(max_length=100)
    cmp_sales = models.CharField(max_length=100)
    cmp_workers = models.IntegerField()
    cmp_explanations = models.TextField()
    def __str__(self):
        return self.cmp_name


class CompanyESG(models.Model):
    esg = models.ForeignKey(CompanyList, on_delete=models.CASCADE)
    cmp_ESG = models.CharField(max_length=10)
    cmp_E = models.CharField(max_length=10)
    cmp_S = models.CharField(max_length=10)
    cmp_G = models.CharField(max_length=10)