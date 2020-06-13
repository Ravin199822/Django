from django.db import models

# Create your models here.

class tbl2Consultants(models.Model):
    id = models.AutoField
    name=models.CharField(max_length=500, default='')

class tbl2HealthCenters(models.Model):
    id = models.AutoField
    name=models.CharField(max_length=100, default='')

class tbl2Patients(models.Model):
    id = models.AutoField
    name=models.CharField(max_length=500, default='')

class tbl2Cases(models.Model):
    id = models.AutoField
    CaseNumber = models.CharField(max_length=50, default='')
    PatientID = models.ForeignKey(tbl2Patients,default=None,null=True,on_delete=models.SET_NULL)
    HealthCenterID = models.ForeignKey(tbl2HealthCenters,default=None,null=True,on_delete=models.SET_NULL)
    ConsulatedBy = models.ForeignKey(tbl2Consultants,default=None,null=True,on_delete=models.SET_NULL)
    Fee = models.IntegerField(default=0)
    RegisterDate = models.DateField()

    def __str__(self):
        return self.CaseNumber

