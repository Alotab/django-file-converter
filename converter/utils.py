import tempfile
from django.shortcuts import render
from django.http import FileResponse
from PyPDF2 import PdfMerger
from PIL import Image
import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def upload_jpg(files):
    """
    This function converts the `.jpg` and `.jpeg` files into one `.pdf` file.
    """
    pdfFile = None
    merger = PdfMerger()
    for filename in files:
        im = Image.open(filename)
        
        if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
            im.load()
            background = Image.new("RGB", im.size, (255, 255, 255))
            background.paste(im, mask=im.split()[3])
            im = background

        # Create a temporary file with a unique name
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp:
            # Save the image as a temporary PDF file
            im.save(temp.name, 'PDF', encoding='latin-1')

            # Add the temporary PDF file to the merger
            merger.append(temp.name)

    # Save the merged PDF file
    pdfFile = 'output.pdf'
    merger.write(pdfFile)
    merger.close()
    return pdfFile
    


import openpyxl

def read_excel_file(file):
    """
    This function reads the data from an Excel file.
    """
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    data = sheet
    return data

from spire.xls import *
from spire.common import *

def xlsx_to_pdf(files):
    pdfFile = None

    for file in files:

        ## Read the data from the Excel file
        data = pd.read_excel(file)
        # data = read_excel_file(file)
       

        # Create a PDF document
        pdfFile = SimpleDocTemplate('excelfile.pdf', pagesize=letter)

        # Create a table with the data
        tabel = Table(data)

        # Add some style to the table
        tabel.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#d0d0d0'),
            ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), '#f5f5f5'),
        ]))

        # Add tabel to the PDF document
        pdfFile.build([tabel])

    return pdfFile







def convert_file(files, conversion):
    newFile = None
    
    for file in files:
        filename = file.name
        _, file_extension = os.path.splitext(filename)
        print(file_extension)
        # if file_extension in ('.jpg', '.jpeg') and 'pdf' in conversion:
        #     newFile = upload_jpg(files)

        if file_extension in ('.xlsx') and 'pdf' in conversion:
            newFile = xlsx_to_pdf(files)
        else:
            print(f'File extension {file_extension} is not')

    return newFile