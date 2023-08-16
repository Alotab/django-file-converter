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

# from io import BytesIO
# from img2pdf import convert
# from pdfkit import from_file
import tempfile
from PyPDF2 import PdfMerger
from PIL import Image




def upload_csv(request):
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
    model = uploadConverter
    template_name = 'converter/csvlist.html'




def upload_jpg(request):
    """
    This function converts the image files uploaded by the user into one PDF file.
    """
    output_filename = None
    if request.method == 'POST':
        jpg_files = request.FILES.getlist('jpg_file')
        merger = PdfMerger()
        for filename in jpg_files:
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
        output_filename = 'output.pdf'
        merger.write(output_filename)
        merger.close()

    return render(request, 'converter/uploadfile.html', {'output_filename': output_filename})

















# .................

from django.http import FileResponse

# def download_pdf(request, output_filename):
#     """
#     This function allows the user to download the specified PDF file.
#     """
#     # Open the PDF file in binary mode
#     with open(output_filename, 'rb') as pdf:
#         # Create a new FileResponse object
#         response = FileResponse(pdf)

#         # Set the content type to 'application/pdf'
#         response['Content-Type'] = 'application/pdf'

#         # Set the content disposition to 'attachment' to trigger a download
#         response['Content-Disposition'] = f'attachment; filename="{output_filename}"'

#         return response

def download_pdf(request, output_filename):
    """
    This function allows the user to download the specified PDF file.
    """
    # Create a new FileResponse object
    response = FileResponse(open(output_filename, 'rb'))

    # Set the content type to 'application/pdf'
    response['Content-Type'] = 'application/pdf'

    # Set the content disposition to 'attachment' to trigger a download
    response['Content-Disposition'] = f'attachment; filename="{output_filename}"'

    return response



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