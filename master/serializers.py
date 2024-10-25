from rest_framework import serializers

from .models import NewsModel, BlogModel

class NewsSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = NewsModel
        fields = ['author', 'title', 'images', 'article']

class BlogSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = BlogModel
        fields = ['title', 'description', 'video']


class NewsNoImageSerializer(serializers.ModelSerializer):
    
    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('title', instance.title)
        instance.article = validated_data.get('article', instance.article)
        instance.save()
        return instance

    class Meta(object):
        model = NewsModel
        fields = ['author', 'title', 'article']