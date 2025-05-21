from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Event
from .serializers import EventSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

class EventListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EventSerializer)
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Event, pk=pk)

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EventSerializer)
    def put(self, request, pk):
        event = self.get_object(pk)
        if event.created_by != request.user:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):
        event = self.get_object(pk)
        if event.created_by != request.user:
            return Response({"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN)

        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
