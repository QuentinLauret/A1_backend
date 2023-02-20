from django.db import models

class Guitar(models.Model):                    #Create the table named "Guitar" with 5 keys
    gid = models.IntegerField(unique = True)
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    isElectric = models.BooleanField()
    price = models.FloatField()

    def __str__(self):                  #Return the name of the guitar
        return "%s " %(self.name) 
    class Meta:  
        db_table = "guitar"  
    

