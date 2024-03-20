from rest_framework import serializers
from .models import Person,Color

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_inf = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = '__all__'
    

    def get_color_inf(self,obj):
        return {'color_name':Color.objects.get(id = obj.color.id).color_name,'hex':'#005'}
    def validate(self, data):
        special_characters = set(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?'])
        for c in data['name']:
            if c in special_characters:
                raise serializers.ValidationError('name can not contain special characters')

        if data['age']<18:
            raise serializers.ValidationError('age should be greater than 18')
        return data
