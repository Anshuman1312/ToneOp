from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *

class SchoolAPI(APIView):
    def post(self,request):
        try:
            serialize=School_serializer(data=request.data)
            if serialize.is_valid():   
                serialize.save()
                return Response({"message":"data sucessfully created","data":serialize.data},status=status.HTTP_201_CREATED)
            return Response({"message":"Error on Creation "},serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def get(self,request):
        try:
            data=School.objects.all()
            serialize=School_serializer(data,many=True)
            return Response({"message":"All Data","data":serialize.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
class SchoolUpdateAndDeleteAPI(APIView):
    def patch(self,request,id=None):
        try:
            data=School.objects.get(id=id)
            serialize=School_serializer(data,request.data,partial=True)
            if serialize.is_valid():
                serialize.save()
                return Response({"message":"data sucessfully updated","data":serialize.data},status=status.HTTP_200_OK)
            return Response({"message":"Error on Update"},serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id=None):
        try:
            data=School.objects.get(id=id)
            if data:
                data.delete()
                return Response({"message":"data sucessfully deleted"},status=status.HTTP_200_OK)
            return Response({"message":"No Data Found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

class SpecificSchoolAPI(APIView):    
    def get(self,request,id=None):
        try:
            data=School.objects.get(id=id)
            if data:
                serialize=School_serializer(data)
                return Response({"message":"Data Found","data":serialize.data},status=status.HTTP_200_OK)
            return Response({"message":"No Data Found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        

class StudentAPI(APIView):
    def post(self,request):
        try:
            serialize=Student_serializer(data=request.data)
            if serialize.is_valid():   
                serialize.save()
                return Response({"message":"data sucessfully created","data":serialize.data},status=status.HTTP_201_CREATED)
            return Response({"message":"Error on Creation "},serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        try:
            data=Student.objects.all()
            serialize=School_serializer(data,many=True)
            return Response({"message":"All Data","data":serialize.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

class StudentUpdateAndDeleteAPI(APIView):        
    def patch(self,request,id=None):
        try:
            data=Student.objects.get(id=id)
            serialize=Student_serializer(data,request.data,partial=True)
            if serialize.is_valid():
                serialize.save()
                return Response({"message":"data sucessfully updated","data":serialize.data},status=status.HTTP_200_OK)
            return Response({"message":"Error on Update"},serialize.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id=None):
        try:
            data=Student.objects.get(id=id)
            if data:
                data.delete()
                return Response({"message":"data sucessfully deleted"},status=status.HTTP_200_OK)
            return Response({"message":"No Data Found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    
class SpecificStudentAPI(APIView):
    def get(self,request,id=None):
        try:
            data=Student.objects.get(id=id)
            if data:
                serialize=Student_serializer(data)
                return Response({"message":"Data Found","data":serialize.data},status=status.HTTP_200_OK)
            return Response({"message":"No Data Found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

class SearchAPI(APIView):
    def post(self,request):
        try:
            name=request.data.get("name",None)
            enrollment=request.data.get("enrollment",None)
            filters={}
            if name:
                filters["Name__icontains"]=name
            if enrollment:
                filters["Enrollment__icontains"]=enrollment
            studentdata=Student.objects.filter(**filters)
            if studentdata:
                serialize=Student_serializer(studentdata,many=True)
                return Response({"message":"Search Results","data":serialize.data},status=status.HTTP_200_OK)
            schooldata=School.objects.filter(**filters)
            if schooldata:
                serialize=School_serializer(schooldata,many=True)
                return Response({"message":"Search Results","data":serialize.data},status=status.HTTP_200_OK)
            else:
                return Response({"message":"No Data Found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)