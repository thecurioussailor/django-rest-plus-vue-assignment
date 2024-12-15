# TODO There's certainly more than one way to do this task, so take your pick.
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.demo.models import Post, Comment
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'timestamp', 'user']

class PostSerializer(ModelSerializer):
    comments = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['text', 'timestamp', 'user', 'comments', 'comment_count']

    def get_comment_count(self, obj):
        return obj.comments.count()