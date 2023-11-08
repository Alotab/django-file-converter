from django.urls import path, include
from rest_framework.routers import DefaultRouter
from converter.views import UploadViewSet
from . import views

file_list = UploadViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

file_detail = UploadViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = DefaultRouter()
router.register(r'files', views.UploadViewSet, basename='files')

filename_pattern = '[^/]+'
urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    # path('upload/', views.upload_csv, name='upload_csv'),
    # path('uploads/', views.upload_jpg, name='upload_jpg'),


    # path('uploads/', views.post, name='post'),
    # path('uploads/<output_filename>', views.download_pdf, name='download_pdf'),

    # try for download url matching
    path('download/<str:filename>/', views.download, name='download'),
    # path('download/<filename:path("([^/]+)")>/', views.download, name='download'),
    # path('download/<filename:[^/]+>/', views.download, name='download'),
    
    # path('download/<filename:' + filename_pattern + '>/', views.download, name='download'),




    # original url
    # path('download/<str:converted_File>/', views.download, name='download'),
    path('files/', views.CsvFileList.as_view(), name='file-list'),
    path('rest_api/', include(router.urls)),
]