from rest_framework import permissions 


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        Custom permisssion to only allow owners of an object to edit it
    """
    def has_object_permission(self, request, view, obj):

        # Read permission are allowed to any request,
        # so, always allow GET, HEAD or Options requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # write permissions are obly allowed to the owner of the uploaded files
        return obj.owner == request.user