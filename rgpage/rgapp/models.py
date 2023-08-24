from django.db import models

# Create your models here.
class rgmodel(models.Model):
    username= models.CharField(max_length=15)
    name= models.CharField(max_length=30)
    password= models.CharField(max_length=15)

    def __str__(self):
        return"username={0},name={1},password={2}".format(self.username,self.name,self.password)

