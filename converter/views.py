from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.http import FileResponse
from django.urls import reverse
from rest_framework import viewsets
from rest_framework import permissions
from .models import uploadConverter
from converter.serializers import UploadConverterSerializer, UserSerializer
from converter.permissions import IsOwnerOrReadOnly
from django.views.decorators.csrf import csrf_exempt
import csv
import os
import json

from PyPDF2 import PdfMerger
from PIL import Image
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from .utils import convert_file, upload_jpg
from .forms import UploadFileForm
from .models import File
from django import template
import uuid
import tempfile
from django.core.files.temp import NamedTemporaryFile
from django.conf import settings
import io
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage



@csrf_exempt
def upload_file(request):
    json_context = None
    converted_files = []
    temp_dir = tempfile.TemporaryDirectory()

    if request.method == "POST":
        uploaded_files = request.FILES.getlist('files')
        formats = request.POST.getlist('formats')

        # Convert and save each file separately
        for file_object, conversion_format in zip(uploaded_files, formats):
            # converted_file = convert_file(file_object, conversion_format)
            filename= convert_file(file_object, conversion_format)
            # converted_file_object = io.BytesIO(filename.encode())
            # print(type(converted_file_object))

            # converted_file_object = io.StringIO(converted_file)

            filename_cr = generate_unique_filename(file_object.name, conversion_format)

            uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
            if not os.path.exists(uploads_dir):
                os.makedirs(uploads_dir)

            upload_file_path = os.path.join(uploads_dir, filename_cr)
            # upload_file_path = os.path.join(uploads_dir, converted_file)
            # with open(upload_file_path, 'wb') as f:
            #     f.write(converted_file_object.read())
            #     f.seek(0)

            # download_url = reverse('download', kwargs={'filename': filename})
            download_url = reverse('download', kwargs={'filename': filename})
            

            converted_file_info = {
                'original_filename': file_object.name,
                'converted_filename': filename,
                'temporary_file': uploads_dir,
                'download_url': download_url,
            }

            converted_files.append(converted_file_info)
           
            context = {
                'converted_files': converted_files
            }
            print(context)
            
            # Serialize the context as a JSON object
            json_context = json.dumps(context)

        # Return the JSON context in the AJAX response
        return JsonResponse(json_context, safe=False)
        # return render(request, 'converter/uploadfile.html', context)
    else:

        context = {'converted_files': [],}
        return render(request, 'converter/uploadfile.html', context)



@csrf_exempt
def upload_filess(request):
    converted_File = None
    converted_files = []
    temp_dir = tempfile.TemporaryDirectory()
    
    if request.method == "POST":
        uploaded_files = request.FILES.getlist('files')
        formats = request.POST.getlist('formats')
        print(f'upload files: {uploaded_files}')
        print(f'upload formats: {formats}')
    
        for file_object in uploaded_files:
            for conversion_format in formats:
                converted_File = convert_file(file_object, conversion_format)
                print(f'for file: {file_object}')
                print(f'for formats: {conversion_format}')
                converted_file_object = io.StringIO(converted_File)


                # generate a unique filename for the converted file 
                filename = generate_unique_filename(file_object.name)

                uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
                if not os.path.exists(uploads_dir):
                    os.makedirs(uploads_dir)

                upload_file_path = os.path.join(uploads_dir,filename)
                with open(upload_file_path, 'wb') as f:
                    f.write(converted_file_object.read().encode())
                    f.seek(0)

                # Generate a download URL  for the converetd file 
                # download_url = reverse('download', kwargs={'filename': filename})

                converted_file_info = {
                    'original_filename': file_object.name,
                    'converetd_filename': filename,
                    # 'download_url': download_url,
                    'temporary_file': uploads_dir,
                }

                converted_files.append(converted_file_info)
                context = {
                    'uploaded_files': uploaded_files,
                    'converted_files': converted_files
                }
                return render(request, 'converter/uploadfile.html', context)
                # return HttpResponse(request, 'converter/uploadfile.html', {'converted_File': converted_File})
    return render(request, 'converter/uploadfile.html', {'converted_File': converted_File})



def generate_unique_filename(original_filename, conversion_format):
    conversion_format = conversion_format.lower()
    filename_base, filename_ext = os.path.splitext(original_filename)
    unique_filename = f'{filename_base}_{uuid.uuid4()}.{conversion_format}'
    return unique_filename



# @csrf_exempt
# def upload_file(request):
#     converted_File = None
#     container = []
#     if request.method == "POST":
#         files = request.FILES.getlist('files')
#         filenames = request.POST.getlist('filenames')
#         formats = request.POST.getlist('formats')
#         # print(filenames)
#         converted_File = convert_file(files, formats)

#     return render(request, 'converter/uploadfile.html', {'converted_File': converted_File})
  


# @csrf_exempt
# def upload_filessssss(request):
#     converted_File = None
#     if request.method == "POST":
#         files = request.FILES.getlist('files')
#         filenames = request.POST.getlist('filenames')
#         formats = request.POST.getlist('formats')
#         converted_File = upload_jpg(files,formats)
      
#     return render(request, 'converter/uploadfile.html', {'converted_File': converted_File})


# def upload_file(request):
#     converted_File = None
#     converted_file = None
#     converted_file_list = []
#     if request.method == 'POST':
#         # form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)

#             # Get the uploaded file and selected conversion option
#             uploaded_files = request.FILES.getlist('file')
#             print(uploaded_files)
#             # conversion = form.cleaned_data['conversion']
#             # print(conversion)
#             for file in uploaded_files:
#                 # hii, file_extension = os.path.splitext(file)
#                 # print(hii)
#                 # converted_File = convert_file(uploaded_files, conversion)
#                 converted_File = convert_file(uploaded_files)
          
#     else:
#         form = UploadFileForm()
#     return render(request, 'converter/uploadfile.html', {'form': form, 'converted_File': converted_File})




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

def downloadSS(request, filename):
    uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    # Retrieve the converted file from storage
    fs = FileSystemStorage(location=uploads_dir)
    converted_file = fs.open(filename)

    # Set the appropriate response content type
    extension = os.path.splitext(filename)[1]
    content_type = {
        '.pdf': 'application/pdf',
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',

        
'.txt': 'text/plain',
    }.get(extension, 'application/octet-stream')
    response = HttpResponse(converted_file.read(), content_type=content_type)

    # Set the Content-Disposition header to specify the filename
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    return response




def download(request, filename):
    """
    This function allows the user to download a converted file.
    """
    # Create a new FileResponse object
    response = FileResponse(open(filename, 'rb'))

    # Set the content type to 'application/pdf'
    extension = os.path.splitext(filename)[1]
    content_type = {
        '.pdf': 'application/pdf',
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        '.txt': 'text/plain',
    }.get(extension, 'application/octet-stream')
    # response['Content-Type'] = 'application/pdf'
    response['Content-Type'] = content_type

    # Set the content disposition to 'attachment' to trigger a download
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(filename)}"'

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