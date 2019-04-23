from tastypie.resources import ModelResource
from .models import Video
import requests
from tastypie.authorization import Authorization

# These files are used for the querying of data on the server side of the applications

# class MultipartResource(object):
#     def deserialize(self, request, data, format=None):
#         if not format:
#             format = request.META.get('CONTENT_TYPE', 'application/json')
#         if format == 'application/x-www-form-urlencoded':
#             return request.POST
#         if format.startswith('multipart'):
#             data = request.POST.copy()
#             data.update(request.FILES)
#             return data
#         return super(MultipartResource, self).deserialize(request, data, format)


class VideoResource(ModelResource):
    http_method_names = ['get', 'post', 'head', 'put']
    class Meta:
        queryset = Video.objects.all()
        resource_name = "video"
        authorization = Authorization()