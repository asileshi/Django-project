from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonSerializer,LoginSerializer
from .models import Person
# Create your views here.
@api_view(['GET'])
def index(request):
     courses = {
          'course_name':'Python',
          'learn':['flask','django','fastApi','Tornado'],
          'course_provider':'Scaler'
     }
     return Response(courses)
@api_view(['POST','GET'])
def login(request):
    data = request.data
    serilized = LoginSerializer(data=data)
    if serilized.is_valid():
        data = serilized.validated_data
        return Response({'message':'success'})
    
    return Response(serilized.errors)

class PersonApi(APIView):
    def get(self,request):
        obj = Person.objects.all()
        serialized = PersonSerializer(obj,many = True)
        return Response(serialized.data)
    def post(self,request):
        data = request.data
        serialized = PersonSerializer(data = data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized.errors)
    def put(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serialized = PersonSerializer(obj,data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized.errors)
    def patch(self,request):
        data = request.data
        obj = request.objects.get(id = data['id'])
        serilized = PersonSerializer(obj,data=data,partial = True)
        if serilized.is_valid():
            return Response(serilized.data)
        else:
            return Response(serilized.errors)
        
    def delete(self,request):
        data = request.data
        try:
            obj = Person.objects.get(id = data['id'])
            obj.delete()
            return Response({'message':'person deleted!'})
        except:
            return Response({'message':'person does not exist'})
    
            


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == 'GET':
        obj = Person.objects.all()
        serialized = PersonSerializer(obj,many = True)
        return Response(serialized.data)
    elif request.method == 'POST':
        data = request.data
        serialized = PersonSerializer(data = data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serialized = PersonSerializer(obj,data=data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized.errors)
    elif request.method == 'DELETE':
        data = request.data
        try:
            obj = Person.objects.get(id = data['id'])
            obj.delete()
            return Response({'message':'person deleted!'})
        except:
            return Response({'message':'person does not exist'})
    
            

