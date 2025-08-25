from rest_framework import serializers
from .models import personModel, cityModel, studentModel
import re
from rest_framework.response import Response



class personSerializer(serializers.ModelSerializer):
    city_name=serializers.PrimaryKeyRelatedField(queryset=cityModel.objects.all(),write_only=True)
    read_city=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=personModel
        fields= ['id','name','age','read_city','city_name']
        
    def get_read_city(self, obj):
        return obj.city_name.city
    
    def validate_name(self,name):
        pattern = r'[^a-zA-Z0-9 ]'
        if re.search(pattern,name):
            raise serializers.ValidationError({'message':"special characters are not allowed"})
        return name
            
        


class studentSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    roll_no=serializers.IntegerField()
    
    def validate(self, attrs):
        pattern = r'[^0-9]'
        if len(str(attrs['roll_no'])) >= 9:
            raise serializers.ValidationError({'message': 'Roll no too long'})
        if re.search(pattern,str(attrs['roll_no'])):
                raise serializers.ValidationError({'message': 'Special characters not allowed'})
        return attrs 
    
    def create(self,validated_data):
        return studentModel.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll_no=validated_data.get('roll_no',instance.roll_no)
        instance.save()
        return instance
        
        
    