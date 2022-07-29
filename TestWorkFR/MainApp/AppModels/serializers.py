from rest_framework import serializers
from .models import Message, Newsletter, Client


class ClientCreate(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientListSerializator(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'tag')


class NewsletterCreateSelializator(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'


class MessageListSelializator(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageDetailSelializator(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
