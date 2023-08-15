from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .models import uploadConverter
from converter.serializers import UploadConverterSerializer, UserSerializer
from converter.permissions import IsOwnerOrReadOnly
import csv



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