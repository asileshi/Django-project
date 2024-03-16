from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
    def validate(self, data):
        special_characters = set(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?'])
        for c in data['name']:
            if c in special_characters:
                raise serializers.ValidationError('name can not contain special characters')

        if data['age']<18:
            raise serializers.ValidationError('age should be greater than 18')
        return data
