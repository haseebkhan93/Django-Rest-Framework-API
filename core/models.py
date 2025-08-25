from django.db import models

choices={
    ('Lahore','Lahore'),
    ('Karachi','Karachi'),
    ('Islamabad','Islamabad'),
    ('Peshawar','Peshawar'),
    ('Quetta','Quetta')
}

class cityModel(models.Model):
    city=models.CharField(max_length=50, choices=choices)
    


class personModel(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    city_name=models.ForeignKey(cityModel,on_delete=models.RESTRICT)
    
    
class studentModel(models.Model):
    name=models.CharField(max_length=50)
    roll_no=models.IntegerField()    
    
