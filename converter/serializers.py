from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import uploadConverter




# class UploadConverterSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owener.username')
#     class Meta:
#         model = uploadConverter
#         fields = ['id', 'first_name', 'last_name', 'gender', 'age', 'phone', 'email', 'owner']





# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     # files = serializers.PrimaryKeyRelatedField(many=True, queryset=uploadConverter.objects.all())
#     # snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'files']   # snippets is a reverser relationship on the iser model, it will not be included by default when using the ModelSerializer class, so we needed to add an explicit field for it
