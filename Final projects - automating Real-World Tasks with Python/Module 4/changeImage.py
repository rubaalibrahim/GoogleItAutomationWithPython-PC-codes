from PIL import Image
import os
import sys

user = os.getenv('USER')
source = '/home/{}/supplier-data/images/'.format(user)
images = os.listdir(source)

for image in images:
    if 'tiff' in image:
        # grab the picture name without the .tiff extension
        file_name = os.path.splitext(image)[0]
        outfile = source + file_name + ".jpeg"
        try:
            Image.open(source + image).convert("RGB").resize((600, 400)).save(outfile, "JPEG")
        except IOError:
            print("unable to convert", image)