from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
import urllib, base64

register = template.Library()

@register.filter
def get64(path):
  """
  Method returning base64 image data instead of URL
  """
  # if url.startswith("http"):
  #   image = StringIO(urllib.urlopen(url).read())
  #   return 'data:image/jpg;base64,' + base64.b64encode(image.read())

  # return url
  print("MSK", path)
  # import code; code.interact(local=dict(globals(), **locals()))
  with open(path, 'rb') as image_file:
    return base64.b64encode(image_file.read())
