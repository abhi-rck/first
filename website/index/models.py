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
    post=models.TextField(default="post updated soon")
    def __str__(self):
        return self.name

class fourthyear(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    branch=models.TextField(default="NA")
    def __str__(self):
        return self.name

class thirdyear(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    branch=models.TextField(default="NA")
    def __str__(self):
        return self.name

class secondyear(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    branch=models.TextField(default="NA")
    def __str__(self):
        return self.name

class firstyear(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    branch=models.TextField(default="NA")
    def __str__(self):
        return self.name

class achievementss(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField()
    var=models.TextField(default="left")
 
    def _str_(self):
        return str(self.name)

class developers(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField()
    year=models.TextField()
    branch=models.TextField(default="NA")

    def __str__(self):
        return self.name


class acphoto(models.Model):
    img=models.ImageField()

class suggest(models.Model):
    name=models.CharField(max_length=50)
    suggestion=models.TextField()
    def __str__(self):
        return str(self.id)


class news(models.Model):
    heading = models.CharField(max_length=50)
    desc=models.TextField()
    def __str__(self):
        return str(self.id)


class learn(models.Model):
    heading=models.TextField()
    desc=models.TextField()
    col=models.TextField(default=12)
    def __str__(self):
        return str(self.id)
    
    


    

