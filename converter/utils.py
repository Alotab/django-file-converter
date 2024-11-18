import tempfile
from django.shortcuts import render
from django.http import FileResponse
from PyPDF2 import PdfMerger
from PIL import Image
import os
import pandas as pd
from openpyxl import load_workbook
from reportlab.lib.pagesizes import letter,landscape,A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from django.core.files import File
import pandas
import pdfkit
import tabula


def convert_file(file_object, conversion_format):
    filename = file_object.name
    # filename = 'another.jpg'
    _, file_extension = os.path.splitext(filename)

    converted_file = None

    if file_extension in ('.jpg', '.jpeg') and conversion_format == 'PDF':
        converted_file = upload_jpg(file_object, conversion_format)
    elif file_extension in ('.xlsx', '.xls') and conversion_format == 'PDF':
        converted_file = xlsx_to_pdf(file_object)
    elif file_extension in ('.pdf') and conversion_format == 'CSV':
        converted_file = pdf_to_csv(file_object)
    else:
        print(f'File extension {file_extension} is not supported for format {conversion_format}')

    return converted_file


def upload_jpg(file, format):
    """
    This function converts the `.jpg` and `.jpeg` files into one `.pdf` file.
    """
    pdfFile = None
    merger = PdfMerger()

    # print(f"Number of files: {len(files)}")
    # for file in files:
        # print(file)
    # print(f"Number of formats: {len(formats)}")

    # for file, format in zip(files, formats):

    filename = file.name
    name, _ = os.path.splitext(filename)

    im = Image.open(file)
        
    if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
        im.load()
        background = Image.new("RGB", im.size, (255, 255, 255))
        background.paste(im, mask=im.split()[3])
        im = background

    # Create a temporary file with a unique name and Save the image as a temporary PDF file.  Add the temporary PDF file to the merger
    with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp:
        im.save(temp.name, 'PDF', encoding='latin-1')
        merger.append(temp.name)

    # Save the merged PDF file
    format = format.lower()
    pdfFile = f"{name}.{format}"
    # pdfFile = 'output.pdf'
    merger.write(pdfFile)
    merger.close()
    return pdfFile       #File(open(pdfFile, 'rb'), name=pdfFile)
    
    

def xlsx_to0000_pdf(file):
    filename = file.name
    name,_ = os.path.splitext(filename)
    output = f'{name}.pdf'
    
    df = pd.read_excel(file)
    df.to_html('file.html')
    pdFile = pdfkit.from_file('file.html', output)
    print(type(pdFile))
    return pdFile


def xlsx_to_pdf(file):
    filename = file.name
    name,_ = os.path.splitext(filename)
    output = f'{name}.pdf'
    
    df = pd.read_excel(file)
    df.to_html('file.html')
    pdfkit.from_file('file.html', output)
    
    with open(output, 'rb') as f:
        pdf_file = f.read()
    print(type(pdf_file))
    return pdf_file


def pdf_to_csv(file):
    filename = file.name
    name,_ = os.path.splitext(filename)
    output = f'{name}.csv'

    csvFile = tabula.convert_into(file, output)
    return csvFile





def xlsx_tooooo_pdf(file):
    """
        This function converts all excel files `.xlsx`, `.xlx` into `pdf`
    """
    pdfFile = "output.pdf"
    # for file in files:
    print(file, '....................................................')

    # load excel file
    workbook = load_workbook(file)

    # get the current sheet
    worksheet = workbook.active

    # Read the number of rows and columns in the current sheet
    max_row = worksheet.max_row
    max_column = worksheet.max_column

    # set PDF canvas
    c = canvas.Canvas(pdfFile, pagesize=landscape(A4))

    # set margins
    top_margin = 3*inch
    left_margin = 0.75*inch 
    bottom_margin = 0.75*inch
    right_margin = 0.75*inch


    cell_width = (11*inch - left_margin - right_margin) / max_column
    cell_height = (8.5*inch - top_margin - bottom_margin) / max_row

    for row in range(1, max_row+1):
        for column in range(1, max_column+1):
            cell = worksheet.cell(row=row, column=column)
            text=str(cell.value)
            x = left_margin + (column -1) * cell_width
            # y = 11*inch - (top_margin + max_row * cell_height)
            y = 11*inch - (top_margin + row * cell_height)
            c.drawString(x, y, text)

    # save PDF and close canvas
    c.save()
    print('Done conversion of .xls to pdf file')
    return pdfFile





















# def convert_file(files, formats):
#     newFile = None
#     for file in files:
#         for format in formats:
#             filename = file.name
            
#             # filename = filename.decode("utf-8")
#             _, file_extension = os.path.splitext(filename)
#             print(file_extension)
            
#             if file_extension in ('.jpg', '.jpeg') and format == 'PDF':
#                 print('should be workinh')
#                 newFile = upload_jpg(file, format)
#             elif file_extension in ('.xlsx', '.xls') and format == 'PDF':
#                 print('DONT WORK COS IF XLSX')
#                 newFile = xlsx_to_pdf(file)
#             elif file_extension in ('.pdf') and format == 'CSV':
#                 newFile = pdf_to_csv(file)
#             else:
#                 print(f'File extension {file_extension} is not supported for format {format}')
#                 print('DONT WORK COS YOU HAVE NO FORMAT')

#     return newFile



# def convert_file(files, formats):
#     newFile = None
    
#     for file in files:
#         filename = file.name
#         # file = file.name.replace('\x00', '')
#         # print(file)
#         hii, file_extension = os.path.splitext(filename)
#         # print(hii)
#         # print(conversion)
#         if file_extension in ('.jpg', '.jpeg') and 'pdf' in format:
#             newFile = upload_jpg(files, formats)
#         elif file_extension in ('.xlsx') and 'pdf' in format:
#             newFile = xlsx_to_pdf(files)
#         else:
#             print(f'File extension {file_extension} is not')
#     return newFile





# def xlsx_2_pdf(file):
#     # if request.method == 'POST':
#     #     xlsxFiles = request.FILES.getlist('file')

#     #     if not xlsxFiles:
#     #         return render(request, 'converter/uploadfile.html', {'error': 'Please select a file to upload'})

#     #     for xfile in xlsxFiles:

#     # Read the data from the Excel file
#     data = pd.read_excel(file)

#     # Create a PDF document
#     pdfFile = SimpleDocTemplate('excelfile.pdf', pagesize=letter)

#     # Create a table with the data
#     tabel = Table(data.values)

#     # Add some style to the table
#     tabel.setStyle(TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), '#d0d0d0'),
#         ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
#         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
#         ('FONTSIZE', (0, 0), (-1, 0), 14),
#         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
#         ('BACKGROUND', (0, 1), (-1, -1), '#f5f5f5'),
#     ]))

#     # Add tabel to the PDF document
#     pdfFile.build([tabel])

#     return pdfFile






