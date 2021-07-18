from django.db import models

# Create your models here.
class Registration(models.Model):
    
    Sfirstname = models.CharField(max_length=50)
    Slastname = models.CharField(max_length=50)
    Semail = models.EmailField(max_length=100)
    
    Sphone = models.CharField(max_length=10)
    
    Scollege = models.CharField(max_length=100)
    Syear = models.CharField(max_length=1)
    Sstream = models.CharField(max_length=60)
    Sdomain = models.CharField(max_length=60)
    Steamnum = models.CharField(max_length=1)
    Steamname = models.CharField(max_length=50)
    Steammemname1 = models.CharField(max_length=100)
    Steammememail1 = models.EmailField(max_length=100)
    Steammemname2 = models.CharField(max_length=100)
    Steammememail2 = models.EmailField(max_length=100)
    Steammemname3 = models.CharField(max_length=100)
    Steammememail3 = models.EmailField(max_length=100)
    Steammemname4 = models.CharField(max_length=100)
    Steammememail4 = models.EmailField(max_length=100)




    def __str__(self):
        return self.Sfirstname + ' ' + self.Slastname + ' ' + self.Steamnum