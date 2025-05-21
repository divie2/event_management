from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):

    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = '__all__'
        


    def get_created_by(self, obj):
        return obj.created_by.full_name