from django.db import models
from datetime import date

# Create your models here.


class Upload(models.Model):
    user = models.CharField(max_length=250)
    dateOfUpload = models.DateField(default = date.today)
    extension = models.CharField(max_length=250)
    link = models.FileField()
    name = models.CharField(max_length=256, default='Name not added')

    def __str__(self):
        return self.user + ' uploaded '+ self.name + ' with extension ' + self.extension + ' on ' + \
               str(self.dateOfUpload.month)\
               + "/" + str(self.dateOfUpload.day) + "/" + str(self.dateOfUpload.year)+ \
               ' Its Link is this ' + str(self.link)


