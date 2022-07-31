from rest_framework import generics
from .serializers import Serializers

from .models import Client, Newsletter, Message


class ClientCreate(generics.CreateAPIView):
    serializer_class = Serializers.ClientCreate


class ClientListView(generics.ListAPIView):
    serializer_class = Serializers.ClientListSerializator
    queryset = Client.objects.all()


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Serializers.ClientListSerializator
    queryset = Client.objects.all()


class NewsletterCreate(generics.CreateAPIView):
    serializer_class = Serializers.NewsletterCreateSelializator


class NewsletterListView(generics.ListAPIView):
    serializer_class = Serializers.NewsletterCreateSelializator
    queryset = Newsletter.objects.all()


class NewsletterDitailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Serializers.NewsletterCreateSelializator
    queryset = Newsletter.objects.all()


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Serializers.MessageDetailSelializator
    queryset = Message.objects.all()


class MessageListView(generics.ListAPIView):
    serializer_class = Serializers.MessageListSelializator
    queryset = Message.objects.all()


class SendMessageView(generics.CreateAPIView):
    serializer_class = Serializers.MessageListSelializator
