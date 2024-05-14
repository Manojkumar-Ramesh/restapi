from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet 
from rest_framework.decorators import action

from api.models import Movie
from  api.serializers import MovieSerializer

# Create your views here.


class HellowworldView(APIView):
    def get(self,request,*args,**kwargs):

        context={"message":"Hello world"}

        return Response(data=context)
    
class MorningView(APIView):
    def get(self,request,*args,**kwargs):

        context={"message":"Have a fantastic Morning"}
        return Response(data=context)
    
# url:localhost:8000/addition/
#method:post
#data:{"num1":"100","num2":"200"}
    
class AdditionView(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        result=int(n1)+int(n2)
        context={"result":result}

        return Response(data=context)
    
# url:localhost:8000/division/
#method:post
#data:{"num1":"100","num2":"200"}
    
class DivisionView(APIView):
    def post(self,request,*args,**kwargs):
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        result=int(n1)/int(n2)
        context={"result":result}

        return Response(data=context)
    
# url:localhost:8000/bmi/
# method:post
# data:{"height":"165","weight":75}
    
class BmiView(APIView):
    def post(self,request,*args,**kwargs):
        height_in_cm=int(request.data.get("height"))
        weight_in_kg=int(request.data.get("weight"))
        height_in_meter=height_in_cm/100
        bmi=weight_in_kg/(height_in_meter**2)
        context={"result":bmi}
        return Response(data=context)
    

# localhost:8000/calorie/
# method:post
# data":{"height":"165","weight":"75","age":"29","gender":"male|female"}
    
class CalorieView(APIView):
    def post(self,request,*args,**kwargs):
        height_in_cm=int(request.data.get("height"))
        weight_in_kg=int(request.data.get("weight"))
        age=int(request.data.get("age"))
        gender=request.data.get("gender")
        bmr=0
        if gender=="male":
            bmr=(10*weight_in_kg)+(6.25*height_in_cm)-(5*age)+5
            #10 * weight (kg) + 6.25 * height(cm) - 5 * age(y) + 5 for (man)
        elif gender=="female":
            bmr=(10*weight_in_kg)+(6.25*height_in_cm)-(5*age)-161

        context={"result":bmr}
        return Response(data=context)

# url:localhost:8000/emi/
# method:post
# data={"loan_amount":50L,"interest:9%","loan_tenure":20}

class EmiView(APIView):
    def post(self,request,*args,**kwargs):

        p=int(request.data.get("loan_amount"))
        r=float(request.data.get("interest"))
        n=float(request.data.get("loan_tenure"))
        roi=r/12/100
        emi=p*roi*((1+roi)**n)/((1+roi)**n-1)
        context={   "monthly emi":(emi//100),
                    "total amount to pay":(emi*n),
                    "interest amount":((emi*n)-p)
                 

                 }
        return Response(data=context)
    
# ALBUM CRUD

#=============api for listing all albums
    # url:localhost:8000/api/albums/
    # method:get
    # data=nil

#============api for creating new album
    # url:localhost:8000/api/albums/
    # method:post
    # data:{}


class MovieView(APIView):
    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all()

        return Response(data=qs)



    def post(self,request,*args,**kwargs):

        context={"result":"logic for creating a new album"}

        return Response(data=context)    
    
class MovieListCreateView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        # converting queryset to python native type  
        serializer_instance=MovieSerializer(qs,many=True)# serialization
        return Response(data=serializer_instance.data)

    def post(self,request,*args,**kwargs):

        data=request.data
        serializer_instance=MovieSerializer(data=data) #deserialization
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        return Response(data=serializer_instance.errors)


#========api for movie detail=======
    # url: localhost:8000/api/movies/{id}
    # method:get
#========api for delete a movie=======
    # url: localhost:8000/api/movies/{id}
    # method:delete

class MovieRetriveUpdateDestroyView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            qs=Movie.objects.get(id=id)            
            serialzer_instance=MovieSerializer(qs)      # qs=> python native type :serialization
            return Response(data=serialzer_instance.data)
        except:
            context={"message":"request resource does not exist"}
            return Response(data=context,status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")

        try:
            Movie.objects.get(id=id).delete()
            return Response(data={"message":"deleted succesfully"}, status=status.HTTP_200_OK)
        
        except:
            return Response(data={"message":"resourse not found"}, status=status.HTTP_404_NOT_FOUND)
        
#========api for update a movie detail =======
    # url: localhost:8000/api/movies/{id}
    # method:put
        
    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        data= request.data
        movie_obj=Movie.objects.get(id=id)
        serializer_instance=MovieSerializer(data=data,instance=movie_obj)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



#   def list(self,request,*args,**kwargs):
#         pass
#     def create(self,request,*args,**kwargs):
#         pass
#     def retrieve(self,request,*args,**kwargs):
#         pass
#     def update(self,request,*args,**kwargs):
#         pass
#     def destroy(self,request,*args,**kwargs):
#         pass


class MovieViewsetView(ViewSet):

  

    def list(self,request,*args,**kwargs):
        qs=Movie.objects.all()
        #localhost:8000/api/v1/movies?language={value}
        if "language" in request.query_params:
            value=request.query_params.get("language")
            qs=qs.filter(language=value) 

        #localhost:8000/api/v1/movies?genre={value}
        
        if "genre" in request.query_params:
            value=request.query_params.get("genre")
            qs=qs.filter(genre=value)
        serializer_instance=MovieSerializer(qs,many=True)

        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
    
    def create(self,request,*args,**kwargs):
        data=request.data
        serilizer_instance=MovieSerializer(data=data)
        if serilizer_instance.is_valid():
            serilizer_instance.save()
            return Response(data=serilizer_instance.data,status=status.HTTP_200_OK)
        
        return Response(data=serilizer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        movie_obj=Movie.objects.get(id=id)
        serilizer_instance=MovieSerializer(movie_obj)
        return Response(data=serilizer_instance.data,status=status.HTTP_200_OK)
    
    def update(self,request,*args,**kwargs):
        data=request.data
        id=kwargs.get("pk")
        movie_obj=Movie.objects.get(id=id)
        serializer_instance=MovieSerializer(data=data,instance=movie_obj)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return Response(data={"message":"deleted"},status=status.HTTP_200_OK)
    @action(methods=["get"],detail=False)
    def genre(self,request,*args,**kwargs):
        qs=Movie.objects.values_list("genre",flat=True).distinct()
        return Response(data=qs,status=status.HTTP_200_OK)
        
    

class MovieGenre(APIView):
     def get(self,request,*args,**kwargs):
        qs=Movie.objects.values_list("genre",flat=True).distinct()
        return Response(data=qs,status=status.HTTP_200_OK)
    



class MovieLanguage(APIView):
    def get(self,request,*args,**kwargs):
        qs=Movie.objects.values_list("language",flat=True).distinct()
        return Response(data=qs,status=status.HTTP_200_OK)

