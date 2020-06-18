from django.db import models

# Create your models here.
class seeq(models.Model):
    name1=models.CharField(max_length=50)
    name2=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    college=models.TextField()
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return str(self.id)

class faculty(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    desc=models.TextField()
    def __str__(self):
        return self.name

class fourthyear(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    def __str__(self):
        return self.name

class thirdyear(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    def __str__(self):
        return self.name

class secondyear(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    def __str__(self):
        return self.name

class firstyear(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    def __str__(self):
        return self.name

class achievementss(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
 
    def _str_(self):
        return str(self.name)

    

