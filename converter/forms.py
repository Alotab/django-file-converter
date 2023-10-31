from django import forms 
from django.forms import ModelForm, ChoiceField

select = ''
pdf = 'pdf'
jpg = 'jpg'
jpeg = 'jpeg'
xlsx = 'xlsx'

CONVERSION_CHOICES = [
    (select, '.....'),
    (pdf, 'PDF'),
    (jpg, 'JPG'),
    (jpeg, 'JPEG'),
    (xlsx, 'XLSX'),
]




class UploadFileForm(forms.Form):
    file = forms.FileField()
    format = forms.CharField()
    # conversion = forms.ChoiceField(choices=CONVERSION_CHOICES)





# class UploadFileForm(forms.Form):
#     CHOICES = [('1', 'First'), ('2', 'Second'), ('3', 'Third')]
#     my_choice_field = forms.ChoiceField(choices=CHOICES, widget=forms.Select())
