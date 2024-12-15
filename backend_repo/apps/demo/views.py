# TODO There's certainly more than one way to do this task, so take your pick.
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.demo.models import Post, Comment
from apps.demo.serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):
    page_size = 10  # Number of posts per page
    page_size_query_param = 'page_size'

class PostListView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch posts ordered by timestamp (latest first)
        posts = Post.objects.all().order_by('-timestamp')

        # Paginate posts
        paginator = PostPagination()
        paginated_posts = paginator.paginate_queryset(posts, request)

        # Serialize posts with up to 3 latest comments
        serialized_posts = []
        for post in paginated_posts:
            comments = post.comments.order_by('-timestamp')[:3]
            serialized_post = PostSerializer(post).data
            serialized_post['comments'] = CommentSerializer(comments, many=True).data
            serialized_posts.append(serialized_post)

        return paginator.get_paginated_response(serialized_posts)