from rest_framework import generics
from .serializers import ClientCreate, ClientListSerializator, NewsletterCreateSelializator, MessageListSelializator, \
    MessageDetailSelializator
from .models import Client, Newsletter, Message


class ClientCreate(generics.CreateAPIView):
    serializer_class = ClientCreate


class ClientListView(generics.ListAPIView):
    serializer_class = ClientListSerializator
    queryset = Client.objects.all()


class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientListSerializator
    queryset = Client.objects.all()


class NewsletterCreate(generics.CreateAPIView):
    serializer_class = NewsletterCreateSelializator


class NewsletterListView(generics.ListAPIView):
    serializer_class = NewsletterCreateSelializator
    queryset = Newsletter.objects.all()


class NewsletterDitailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsletterCreateSelializator
    queryset = Newsletter.objects.all()


class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageDetailSelializator
    queryset = Message.objects.all()


class MessageListView(generics.ListAPIView):
    serializer_class = MessageListSelializator
    queryset = Message.objects.all()


class SendMessageView(generics.CreateAPIView):
    serializer_class = MessageListSelializator
