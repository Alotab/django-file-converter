from django import forms 
from django.forms import ModelForm, ChoiceField


pdf = 'pdf'
jpg = 'jpg'
jpeg = 'jpeg'
xlsx = 'xlsx'

CONVERSION_CHOICES = [
    (pdf, 'PDF'),
    (jpg, 'JPG'),
    (jpeg, 'JPEG'),
    (xlsx, 'XLXS'),
]



# class UploadFileForm(ModelForm):
#     choice_field = ChoiceField(choices=CONVERSION_CHOICES)

class UploadFileForm(forms.Form):
    file = forms.FileField()
    conversion = forms.ChoiceField(choices=CONVERSION_CHOICES)