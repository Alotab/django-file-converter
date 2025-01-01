
import csv
import os
import json
import uuid
import tempfile
import io
import pandas as pd
import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.core.files.temp import NamedTemporaryFile
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from PyPDF2 import PdfMerger
from PIL import Image

# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from .utils import convert_file





@csrf_exempt
def upload_file(request):
    logger = logging.getLogger(__name__)
    json_context = None
    converted_files = []
    temp_dir = tempfile.TemporaryDirectory()
    if request.method == "POST":
        uploaded_files = request.FILES.getlist('files')
        formats = request.POST.getlist('formats')
        uuid = request.POST.getlist('uuid')

        try: 
            # Convert and save each file separately
            for file_object, conversion_format, uuid in zip(uploaded_files, formats, uuid):
                
                try:
                    filename = convert_file(file_object, conversion_format)
           
                    # filename_cr = generate_unique_filename(file_object.name, conversion_format)
                    if filename:
                        print('is this a file path?', filename)

                        # Create uploads directory if it doesn't exist
                        # uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
                        # if not os.path.exists(uploads_dir):
                        #     os.makedirs(uploads_dir)

                        # file_path = os.path.join(uploads_dir, filename)
                    

                        # Get the coverted file from it location or path
                        # filename = os.path.basename(file_path)
                        # print('final fina path',filename)

                        filename = os.path.basename(filename)
                        print('did i get the name?', filename)
                        
                        # Add coverted file to the reverse function for downloading
                        download_url = reverse('download', kwargs={'filename': filename})
                        
                        converted_file_info = {
                            'original_filename': file_object.name,
                            'converted_filename': filename,
                            'download_url': download_url,
                            'uuid': uuid,
                        }

                        converted_files.append(converted_file_info)
                
                        context = {
                            'converted_files': converted_files
                        }
                    
                        json_context = json.dumps(context)
                except Exception as e:
                    logger.error(f'Error processing file: {e}')
                    converted_files.append({'error': f"Error processing file: {e}"}) 
        except Exception as e:
            logger.error(f'An error occured during the file upload: {e}')
            return JsonResponse({'error': 'An error occurred during file upload.'}, status=500)
            
        return JsonResponse(json_context, safe=False)
    else:
        context = {'converted_files': converted_files,}
        return render(request, 'converter/uploadfile.html', context)



def download(request, filename):
    # Define the path to the file in the 'uploads' folder
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)

    if os.path.exists(file_path):
        # Serve the file for download
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
    else:
        # Handle the case where the file doesn't exist
        return HttpResponse("File not found", status=404)









## working great
# @csrf_exempt
# def upload_FILE(request):
    # json_context = None
    # converted_files = []
    # temp_dir = tempfile.TemporaryDirectory()
    # if request.method == "POST":
    #     uploaded_files = request.FILES.getlist('files')
    #     formats = request.POST.getlist('formats')
    #     uuid = request.POST.getlist('uuid')
      

        # Convert and save each file separately
        # for file_object in form:
        #     filename= convert_file(file_object, conversion_format)
     
        #     filename_cr = generate_unique_filename(file_object.name, conversion_format)

        #     uploads_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
        #     if not os.path.exists(uploads_dir):
        #         os.makedirs(uploads_dir)

        #     upload_file_path = os.path.join(uploads_dir, filename_cr)


            # Assuming 'convert_file' saves the file in 'uploads_dir'
            # with open(upload_file_path, 'wb') as f:
            #     f.write(converted_file_name)  # Assuming converted_file_name is a byte-like object


            # download_url = reverse('download', kwargs={'filename': filename})
            

            # converted_file_info = {
            #     'original_filename': file_object.name,
            #     'converted_filename': filename,
            #     'temporary_file': uploads_dir,
            #     'download_url': download_url,
            #     'uuid': uuid,
            # }

    #         converted_files.append(converted_file_info)
           
    #         context = {
    #             'converted_files': converted_files
    #         }
            
    #         json_context = json.dumps(context)

    #     return JsonResponse(json_context, safe=False)
    # else:
    #     context = {'converted_files': [],}
    #     return render(request, 'converter/uploadfile.html', context)




## working great
# def download_FF(request, filename):
#     """
#     This function allows the user to download a converted file.
#     """
#     # Create a new FileResponse object
#     response = FileResponse(open(filename, 'rb'))

#     # Set the content type to 'application/pdf'
#     extension = os.path.splitext(filename)[1]
#     content_type = {
#         '.pdf': 'application/pdf',
#         '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
#         '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
#         '.txt': 'text/plain',
#     }.get(extension, 'application/octet-stream')
#     # response['Content-Type'] = 'application/pdf'
#     response['Content-Type'] = content_type

#     # Set the content disposition to 'attachment' to trigger a download
#     response['Content-Disposition'] = f'attachment; filename="{os.path.basename(filename)}"'

#     return response


def generate_unique_filename(original_filename, conversion_format):
    conversion_format = conversion_format.lower()
    filename_base, filename_ext = os.path.splitext(original_filename)
    unique_filename = f'{filename_base}_{uuid.uuid4()}.{conversion_format}'
    return unique_filename