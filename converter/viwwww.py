from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.http import FileResponse
from rest_framework import viewsets
from rest_framework import permissions
from .models import uploadConverter
from converter.serializers import UploadConverterSerializer, UserSerializer
from converter.permissions import IsOwnerOrReadOnly
import csv
import os

# from io import BytesIO
# from img2pdf import convert
# from pdfkit import from_file
import tempfile
from PyPDF2 import PdfMerger
from PIL import Image
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from .utils import convert_file 
from .forms import UploadFileForm
from .models import File


from django import template



def upload_file(request):
    converted_File = None
    converted_file = None
    converted_file_list = []
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            # Get the uploaded file and selected conversion option
            uploaded_files = request.FILES.getlist('file')
         
            conversion = form.cleaned_data['conversion']
            print(conversion)
            for file in uploaded_files:
                # hii, file_extension = os.path.splitext(file)
                # print(hii)
                # converted_File = convert_file(uploaded_files, conversion)
                converted_File = convert_file(uploaded_files, conversion)

                # file_obj = File.objects.create(
                #     file_name=file,
                #     file_type=file_extension,
                #     file_content=file.read(),
                #     converted_file_name=f"{file.name}.pdf",
                #     converted_file_type="pdf",
                #     converted_file_content=converted_file,
                # )

            # convert each uploaded file
            # for upload_file in uploaded_files:
            #     converted_file = convert_file(upload_file, conversion)
            #     converted_file_list.append((converted_file, upload_file))
          
    else:
        form = UploadFileForm()
    return render(request, 'converter/uploadfile.html', {'form': form, 'converted_File': converted_File})




# create a model instance from csv dataset
def upload_csv(request):
    """
        Create a model instance from csv dataset from the user input
    """
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        uploadFiles = []
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        next(reader, None)  # skip the header
        for row in reader:
            uploadFiles.append({
                'first_name': row[0],
                'last_name': row[1],
                'gender': row[2],
                'age': row[3],
                'phone': row[4],
                'email': row[5],
                'owner': request.user,
            })
        uploadConverter.objects.bulk_create(uploadConverter(**uploadFile) for uploadFile in uploadFiles)
        return redirect('files')
    return render(request, 'converter/uploadfile.html')

class CsvFileList(ListView):
    """
        List view for populating/Listing all the queryset
    """
    model = uploadConverter
    template_name = 'converter/csvlist.html'






####  Convert jpg files into pdf
# def upload_jpg(request):
#     """
#     This function converts the image files uploaded by the user into one PDF file.
#     """
#     pdfFile = None
#     if request.method == 'POST':
#         jpg_files = request.FILES.getlist('file')
#         if not jpg_files:
#             # No files were uploaded, return an error message
#             return render(request, 'converter/uploadfile.html', {'error': 'Please select a file to upload'})
#         jpg_pdfs = []
#         merger = PdfMerger()
#         for filename in jpg_files:
#             filenamez = filename.name
#             _, file_extension = os.path.splitext(filenamez)
#             if file_extension in ['.jpg', '.jpeg']:
#                 jpg_pdfs.append(filename)

#                 im = Image.open(filename)
                
#                 if im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info):
#                     im.load()
#                     background = Image.new("RGB", im.size, (255, 255, 255))
#                     background.paste(im, mask=im.split()[3])
#                     im = background

#                 # Create a temporary file with a unique name
#                 with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp:
#                     # Save the image as a temporary PDF file
#                     im.save(temp.name, 'PDF')

#                     # Add the temporary PDF file to the merger
#                     merger.append(temp.name)

#             else:
#                 print("File Error: Upload .jpg or .jpeg files")
#                 return render(request, 'converter/uploadfile.html', {'pdfFile': pdfFile})


#         # Save the merged PDF file
#         pdfFile = 'output.pdf'
#         merger.write(pdfFile)
#         merger.close()

#     return render(request, 'converter/uploadfile.html', {'pdfFile': pdfFile})


def download(request, converted_File):
    """
    This function allows the user to download the specified PDF file.
    """
    # Create a new FileResponse object
    response = FileResponse(open(converted_File, 'rb'))

    # Set the content type to 'application/pdf'
    response['Content-Type'] = 'application/pdf'

    # Set the content disposition to 'attachment' to trigger a download
    response['Content-Disposition'] = f'attachment; filename="{converted_File}"'

    return response


## .xlsx to pdf
def xlsx_to_pdf(request):
    if request.method == 'POST':
        xlsxFiles = request.FILES.getlist('file')

        if not xlsxFiles:
            return render(request, 'converter/uploadfile.html', {'error': 'Please select a file to upload'})

        for xfile in xlsxFiles:

            # Read the data from the Excel file
            data = pd.read_excel(xfile)

            # Create a PDF document
            pdfFile = SimpleDocTemplate('excelfile.pdf', pagesize=letter)

            # Create a table with the data
            tabel = Table(data.values)

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

    return render(request, 'converter/uploadfile.html', {'pdfFile': pdfFile})





class UploadViewSet(viewsets.ModelViewSet):
    """
        This viewset automatically provides `list`, `create`, `retrieve, `update` AND `destroy` actions.
        Additionally we also provide an extra `highlight` action.
    """
    queryset = uploadConverter.objects.all()
    serializer_class = UploadConverterSerializer 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

   
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
        This viewset automatically provides `LIST` and `RETRIEVE` actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer