from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
from .models import Report
from .serializers import ReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser, 
                                        IsAuthenticated, 
                                        AllowAny)

from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework import mixins

# Create your views here.


# class ReportView(APIView):

#     permission_classes = (AllowAny)

#     def get(self, request, *args, **kwargs):
#         queryset = Report.objects.all()
#         serializer = ReportSerializer(queryset, many=True)
#         return Response(serializer.data)
    


class PostMixinListView(mixins.CreateModelMixin, mixins.ListModelMixin, GenericAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        print("CREATING:")
        print("DATA", request.data)
        print("ARGS", args),
        print("KWARGS", kwargs)
        return self.create(request, *args, **kwargs)



# class ReportListView(mixins.CreateModelMixin, ListAPIView):

#     serializer_class = ReportSerializer

#     def get_queryset(self):
        
#         weather_type_title = self.request.query_params.get('weather_type', None)
#         if weather_type_title is not None:
#             queryset = Report.objects.filter(weather_type=weather_type_title)
#         else:
#             queryset = Report.objects.all()
#         return queryset


class ReportDetailView(RetrieveAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDeleteView(DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
