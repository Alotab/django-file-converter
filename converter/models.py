from django.db import models
from django.conf import settings


# model for uploading csv file
class uploadConverter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    owner = models.ForeignKey('auth.User',related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"



class File(models.Model):
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=100)
    converted_file_name = models.CharField(max_length=255, blank=True, null=True)
    converted_file_type = models.CharField(max_length=100, blank=True, null=True)
    converted_file_content = models.TextField(blank=True, null=True)


# storing files in the datafiles