from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from .models import personModel,studentModel
from .serializers import personSerializer,studentSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q


class HomeView(APIView):
    def post(self,request):
        data=request.data
        serializers=personSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_406_NOT_ACCEPTABLE )
    
    def get(self,request):
        objs=personModel.objects.all()
        serializers=personSerializer(instance=objs,many=True)
        return Response(serializers.data)
    
    def delete(self,request):
        user_id = request.data.get('id')
        objs = get_object_or_404(personModel,id=user_id)
        objs.delete()
        return Response({'message':'User Successfully deleted'})
    
class ChangeView(APIView):
    def put(self,request,user_id):
        objs=get_object_or_404(personModel,id=user_id)
        serializers= personSerializer(instance=objs,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)    
    
    def patch(self,request,user_id):
        objs= get_object_or_404(personModel,id=user_id)
        serializers=personSerializer(instance=objs,partial=True,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_406_NOT_ACCEPTABLE)  
    
   
        
        
class StudentView(viewsets.ModelViewSet):
    queryset=studentModel.objects.all()
    serializer_class=studentSerializer
    
    def list(self,request):
        search = request.query_params.get('search')
        queryset=self.queryset
        if search:
            queryset=self.queryset.filter(
                Q(name__icontains=search) | Q(roll_no__icontains=search)   
            )
        serializer=self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
        
    
           
        
        
