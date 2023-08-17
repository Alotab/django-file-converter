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


urlpatterns = [
    path('upload/', views.upload_csv, name='upload_csv'),
    # path('uploads/', views.upload_jpg, name='upload_jpg'),


    # path('uploads/', views.post, name='post'),
    # path('uploads/<output_filename>', views.download_pdf, name='download_pdf'),

    # path('download_pdf/<str:output_filename>/', views.download_pdf, name='download_pdf'),
    path('files/', views.CsvFileList.as_view(), name='file-list'),
    path('rest_api/', include(router.urls)),
]