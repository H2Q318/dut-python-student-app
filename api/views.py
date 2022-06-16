from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from students.models import Student
from .serializers import StudentSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def students(req):
    if req.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def studentDetail(req, id):
    try:
        student = Student.objects.get(id=id)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
            
    if req.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif req.method == 'PUT':
        serializer = StudentSerializer(student, data=req.data)
        if student.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
