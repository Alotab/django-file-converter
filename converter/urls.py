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
    path('upload/', views.upload_csv),
    path('', include(router.urls))
]