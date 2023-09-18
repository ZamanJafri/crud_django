from django.db import models

# Create your models here.
class Emp_Tabel(models.Model):
     pass


class Emp_Data_Table(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    email = models.CharField(max_length = 20)
    phone = models.CharField(max_length=15)
    dsg = models.CharField(max_length=30)
    salary = models.IntegerField()
    city = models.CharField(max_length=20,default="",null=True)
    state= models.CharField(max_length=20,default="",null=True)
    def __str__(self):
         return str(self.id)+ " " + self.firstname + " " +self.lastname + " " + self.email   
"""
create table Emp_Table(
id int not null auto_increament primary key,
firstname varchar(15) not null,
lastname varchar(15) not null,
email varchar(20) not null,
phone varchar(15) not null,
dsg varchar(30) not null,
salar int not null,
city varchar(20),
state varchar(20),
)
"""    