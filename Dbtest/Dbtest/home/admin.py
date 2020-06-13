from django.contrib import admin

# Register your models here.
from .models import tbl2Cases
from .models import tbl2Consultants
from .models import tbl2HealthCenters
from .models import tbl2Patients

admin.site.register(tbl2Cases)
admin.site.register(tbl2Consultants)
admin.site.register(tbl2HealthCenters)
admin.site.register(tbl2Patients)
