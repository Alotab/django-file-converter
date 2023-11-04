from django.template import Library

register = Library()

@register.filter(name='download')
def download_filter(converted_File):
  if converted_File:
    return converted_File.url
  else:
    return ''