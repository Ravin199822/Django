from django.db import models

class tbl2Cases(models.Model):
    id=models.AutoField                        # AutoFiled is an Integerfield that automatically increment according to available IDS
    CaseNumber=models.CharField(default=0)
    PatientID=models.IntegerField(default=0)
    HealthCenterID=models.IntegerField(default=0)
    ConsulatedBy=models.IntegerField(default=0)
    Fee=models.IntegerField(default=0)
    RegisterDate=models.DateField()
