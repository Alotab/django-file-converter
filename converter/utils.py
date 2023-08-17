import tempfile
from django.shortcuts import render
from PyPDF2 import PdfMerger
from PIL import Image
import os

def convert_file(file, conversion):
    if conversion == 'jpg' | conversion == 'jpeg':
        upload_jpg(file, conversion)
    elif conversion == 'xlsx':
        pass





def upload_jpg(file):
    """
    This function converts the image files uploaded by the user into one PDF file.
    """
    jpg_pdfs = []
    pdfFile = None
    merger = PdfMerger()
    for filename in file:
        # filenamez = filename.name
        # _, file_extension = os.path.splitext(filenamez)
       
        jpg_pdfs.append(filename)

        im = Image.open(filename)
        
        if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
            im.load()
            background = Image.new("RGB", im.size, (255, 255, 255))
            background.paste(im, mask=im.split()[3])
            im = background

        # Create a temporary file with a unique name
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp:
            # Save the image as a temporary PDF file
            im.save(temp.name, 'PDF')

            # Add the temporary PDF file to the merger
            merger.append(temp.name)

    # Save the merged PDF file
    pdfFile = 'output.pdf'
    merger.write(pdfFile)
    merger.close()

    return pdfFile
