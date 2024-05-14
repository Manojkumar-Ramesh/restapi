from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

from API.models import Bike
from API.serializers import Bikeserializer


# Create your views here.

#======listing all bikes======
# url:localhost:8000/API/bikes/
# method:get
# data= nill

class BikeListCreateView(APIView):

    def get(self,request,*args,**kwargs):
        qs=Bike.objects.all()
        serialisation_instance=Bikeserializer(qs,many=True)
        return Response(data=serialisation_instance.data)
    
#=======creating a bike============
    # url:localhost:8000/API/bikes/
    # method:post
    # data:{}

    def post(self,request,*args,**kwargs):
        
        data=request.data
        serializer_instance=Bikeserializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        return Response(data=serializer_instance.errors)


# =======list a perticular bike detail======
    # url:localhost:8000/API/bikes/{id}/
    # method:get
    # data=nill
class BikeRetriveUpdateDestroyView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            bike_obj=Bike.objects.get(id=id)
            serialization_instance=Bikeserializer(bike_obj)  # qs=> python native type :serialization
            return Response(data=serialization_instance.data)
        except:
            context={"message":"requested resource doesn't exist"}
            return Response(data=context,status=status.HTTP_404_NOT_FOUND)
        
# =======list a perticular bike detail======
    # url:localhost:8000/API/bikes/{id}/
    # method:delete
    # data=nill

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            Bike.objects.get(id=id).delete()
            return Response(data={"message":"requested item deleted"},status=status.HTTP_200_OK)
        except:
            return Response(data={"message":"requested item not found"},status=status.HTTP_404_NOT_FOUND)
        
# =======update a perticular bike detail======
    # url:localhost:8000/API/bikes/{id}/
    # method:put
    # data={}
        
    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        data=request.data
        bike_obj=Bike.objects.get(id=id)
        serializer_instance=Bikeserializer(data=data,instance=bike_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class BikeSetViewSet(ViewSet):
    def list(self,request,*args,**kwargs):
        data=Bike.objects.all()
        serialisation_instance=Bikeserializer(data,many=True)

        return Response(data=serialisation_instance.data)

    def create(self,request,*args,**kwargs):
        data=request.data
        serializer_instance=Bikeserializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        return Response(data=serializer_instance.errors)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("id")
        bike_obj=Bike.objects.get(id=id)
        serializer_instance=Bikeserializer(bike_obj)
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    
    def update(self,request,*args,**kwargs):
        data=request.data
        id=kwargs.get("id")
        bike_obj=Bike.objects.get(id=id)
        serializer_instance=Bikeserializer(data=data,instance=bike_obj)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        return Response(data=serializer_instance.errors)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Bike.objects.get(id=id).delete()
        return Response(data={"message":"deleted"},status=status.HTTP_200_OK)
    
class BrandView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Bike.objects.values_list("brand",flat=True).distinct()
        return Response(data=qs,status=status.HTTP_200_OK)
    


        
