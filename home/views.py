from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PersonSerializer
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

@api_view(['GET','POST'])
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
     