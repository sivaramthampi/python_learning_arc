from django.shortcuts import render

from rest_framework.decorators import APIView

from .models import userprofile
from .serializers import userserializers
from rest_framework.response import Response

class  userpro(APIView):
    def get(self,req,key):
        takepro=userprofile.objects.get(id=key)           ## to fetch
        newdata=userserializers(takepro)      ## to serialize the fetched data
        return Response(newdata.data)
    def put(self,req,key):
        takepro=userprofile.objects.get(id=key)
        takeallpro = userserializers(takepro,req.data)
        if takeallpro .is_valid():
            takeallpro.save()
            return Response(takeallpro.data)
        else:
            return Response("Invalid Data")
        
    def delete(self,req,key):
        takepro=userprofile.objects.get(id=key)
        takepro.delete()
        return Response("Data Deleted")

class takeprofile(APIView):
    def get(self,request):                          ## self is to point to the object
        takepro=userprofile.objects.all()           ## to fetch
        newdata=userserializers(takepro,many=True)      ## to serialize the fetched data
        return Response(newdata.data)
    
    def post(self,request):                          
        newdata=userserializers(data=request.data)
        if newdata .is_valid():
            newdata.save()
            return Response(newdata.data)
        else:
            return Response("Data Not Valid")            

