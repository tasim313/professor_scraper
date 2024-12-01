from django.utils import timezone
from rest_framework.response import Response
import uuid

def get_request_id(request):
    """Retrieve or generate a unique request ID."""
    return request.headers.get("X-Request-ID") or str(uuid.uuid4())

def base_response(
    success,
    status_code,
    message,
    resource_name,
    http_method,
    data=None,
    error=None,
    suggestion="",
    path="",
    request_id=None,
):
    """Base response structure."""
    return {
        "resource": resource_name,
        "http_method": http_method,
        "status": "success" if success else "error",
        "status_code": status_code,
        "message": message,
        "data": data if success else None,
        "error_details": error if not success else None,
        "suggestion": suggestion if not success else "",
        "timestamp": timezone.now().isoformat(),
        "path": path,
        "request_id": request_id,
    }

# GET Response - List
def get_list_response(request, resource_name, data):
    return Response(
        base_response(
            success=True,
            status_code=200,
            message=f"Successfully retrieved list of {resource_name}.",
            resource_name=resource_name,
            http_method="GET",
            data=data,
            path=request.path,
            request_id=get_request_id(request),
        ),
        status=200,
    )

# GET Response - Single Item
def get_single_response(request, resource_name, data):
    return Response(
        base_response(
            success=True,
            status_code=200,
            message=f"Successfully retrieved {resource_name}.",
            resource_name=resource_name,
            http_method="GET",
            data=data,
            path=request.path,
            request_id=get_request_id(request),
        ),
        status=200,
    )

# POST Response - Create
def post_create_response(request, resource_name, data):
    return Response(
        base_response(
            success=True,
            status_code=201,
            message=f"{resource_name} created successfully.",
            resource_name=resource_name,
            http_method="POST",
            data=data,
            path=request.path,
            request_id=get_request_id(request),
        ),
        status=201,
    )

# PATCH / PUT Response - Update
def update_response(request, resource_name, data, method="PUT"):
    return Response(
        base_response(
            success=True,
            status_code=200,
            message=f"{resource_name} updated successfully.",
            resource_name=resource_name,
            http_method=method,
            data=data,
            path=request.path,
            request_id=get_request_id(request),
        ),
        status=200,
    )

# DELETE Response - Delete
def delete_response(request, resource_name):
    return Response(
        base_response(
            success=True,
            status_code=204,
            message=f"{resource_name} deleted successfully.",
            resource_name=resource_name,
            http_method="DELETE",
            path=request.path,
            request_id=get_request_id(request),
        ),
        status=204,
    )

# Error Response
def error_response(request, resource_name, status_code, message, error_details, suggestion=""):
    return Response(
        base_response(
            success=False,
            status_code=status_code,
            message=message,
            resource_name=resource_name,
            http_method=request.method,
            error=error_details,
            suggestion=suggestion,
            path=request.path,
            request_id=get_request_id(request),
        ),
        status=status_code,
    )



# from django.db import models

# class Resource(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()

#     def __str__(self):
#         return self.name


# from rest_framework import serializers
# from .models import Resource

# class ResourceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Resource
#         fields = ['id', 'name', 'description']



# from rest_framework.generics import ListCreateAPIView
# from rest_framework.permissions import IsAuthenticated
# from .models import Resource
# from .serializers import ResourceSerializer
# from .response_utils import get_list_response, post_create_response, error_response

# class ResourceListCreateView(ListCreateAPIView):
#     queryset = Resource.objects.all()
#     serializer_class = ResourceSerializer
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
#         """Handles GET request - Retrieve list of resources."""
#         try:
#             # Get the list of resources
#             resources = self.get_queryset()
#             serializer = self.get_serializer(resources, many=True)
            
#             # Use the custom response function for successful GET request
#             return get_list_response(request, "Resource", serializer.data)
        
#         except Exception as e:
#             # Handle any error and return a custom error response
#             return error_response(
#                 request,
#                 "Resource",
#                 status_code=500,
#                 message="Failed to retrieve resources.",
#                 error_details=str(e),
#                 suggestion="Please try again later."
#             )

#     def post(self, request, *args, **kwargs):
#         """Handles POST request - Create a new resource."""
#         try:
#             # Deserialize the incoming data and validate
#             serializer = self.get_serializer(data=request.data)
#             if serializer.is_valid():
#                 # Save the new resource
#                 resource = serializer.save()

#                 # Use the custom response function for successful POST request
#                 return post_create_response(request, "Resource", serializer.data)
#             else:
#                 # If validation fails, return an error response
#                 return error_response(
#                     request,
#                     "Resource",
#                     status_code=400,
#                     message="Invalid data.",
#                     error_details=serializer.errors,
#                     suggestion="Please check the input data."
#                 )
        
#         except Exception as e:
#             # Handle unexpected errors and return error response
#             return error_response(
#                 request,
#                 "Resource",
#                 status_code=500,
#                 message="Failed to create resource.",
#                 error_details=str(e),
#                 suggestion="Please try again later."
#             )



# from django.urls import path
# from .views import ResourceListCreateView

# urlpatterns = [
#     path('resources/', ResourceListCreateView.as_view(), name='resource-list-create'),
# ]

# GET Response (Success)
# {
#   "resource": "Resource",
#   "http_method": "GET",
#   "status": "success",
#   "status_code": 200,
#   "message": "Successfully retrieved list of Resource.",
#   "data": [
#     {"id": 1, "name": "Resource 1", "description": "Description of Resource 1"},
#     {"id": 2, "name": "Resource 2", "description": "Description of Resource 2"}
#   ],
#   "error_details": null,
#   "suggestion": "",
#   "timestamp": "2024-11-12T12:34:56+00:00",
#   "path": "/resources/",
#   "request_id": "f79ab163-5cb0-4b80-8e59-1edc7e91cdcf"
# }

# POST Response (Success)
# {
#   "resource": "Resource",
#   "http_method": "POST",
#   "status": "success",
#   "status_code": 201,
#   "message": "Resource created successfully.",
#   "data": {
#     "id": 3,
#     "name": "Resource 3",
#     "description": "Description of Resource 3"
#   },
#   "error_details": null,
#   "suggestion": "",
#   "timestamp": "2024-11-12T12:35:00+00:00",
#   "path": "/resources/",
#   "request_id": "f79ab163-5cb0-4b80-8e59-1edc7e91cdcf"
# }

# Error Response (Validation Error)
# {
#   "resource": "Resource",
#   "http_method": "POST",
#   "status": "error",
#   "status_code": 400,
#   "message": "Invalid data.",
#   "data": null,
#   "error_details": {
#     "name": ["This field is required."],
#     "description": ["This field is required."]
#   },
#   "suggestion": "Please check the input data.",
#   "timestamp": "2024-11-12T12:35:30+00:00",
#   "path": "/resources/",
#   "request_id": "f79ab163-5cb0-4b80-8e59-1edc7e91cdcf"
# }
