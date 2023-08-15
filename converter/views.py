from django.shortcuts import render, HttpResponse
from .models import uploadConverter
import csv



# def upload_csv(request):
#     if request.method == 'POST':
#         csv_file = request.FILES['csv_file']
#         uploadFiles = []
#         with open(csv_file.name, 'r') as f:
#             reader = csv.reader(f)
#             next(reader, None)  # skip the header
#             for row in reader:
#                 uploadFiles.append({
#                     'first_name': row[0],
#                     'last_name': row[1],
#                     'gender': row[2],
#                     'age': row[3],
#                     'phone': row[4],
#                     'email': row[5],
#                 })
#             uploadConverter.objects.bulk_create(uploadConverter(**uploadFile) for uploadFile in uploadFiles)
#             return HttpResponse('ok')
#     return render(request, 'converter/uploadfile.html')


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
            })
        uploadConverter.objects.bulk_create(uploadConverter(**uploadFile) for uploadFile in uploadFiles)
        return HttpResponse('ok')
    return render(request, 'converter/uploadfile.html')
