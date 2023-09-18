from django.contrib import admin
from .models import Emp_Tabel,Emp_Data_Table
# Register your models here.
admin.site.register((Emp_Tabel,)),
admin.site.register((Emp_Data_Table,))