from profiles.models import Profile
from posts.models import Post
from rest_framework.generics import get_object_or_404

from .serializers import ProfileSerializer, PostSerializer
from rest_framework import viewsets
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def number_of_profiles(request):
    quantity_profiles = Profile.objects.all().count()
    return Response({'number_of_profiles': quantity_profiles})


@api_view(['GET'])
def number_of_posts(request):
    quantity_posts = Post.objects.all().count()
    return Response({'number_of_posts': quantity_posts})


class ProfileViewSet(viewsets.ViewSet):
    queryset = Profile.objects.all()

    def list(self, request):
        serializer = ProfileSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        profile = get_object_or_404(self.queryset, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class PostViewSet(viewsets.ViewSet):
    queryset = Post.objects.all()

    def list(self, request):
        serializer = PostSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        profile = get_object_or_404(self.queryset, pk=pk)
        serializer = PostSerializer(profile)
        return Response(serializer.data)
