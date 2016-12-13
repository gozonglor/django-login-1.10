from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm, forms

class Upload(models.Model):
    pic = models.ImageField("Image", upload_to="images/")
    description = models.CharField(max_length=600, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)

upload_date=models.DateTimeField(auto_now_add =True)

# FileUpload form class.
class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = "__all__"

class Comment(models.Model):
    comment = models.CharField(max_length=1000, null=False, default="")
