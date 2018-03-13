from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Post2, User

class PostSerializer(DocumentSerializer):
	class Meta:
		model = Post2
		fields = '__all__'

class PostCreateSerializer(DocumentSerializer):

	class Meta:
		model = Post2
		fields = ('title', 'author', 'tags', 'comments')

class PostUpdateSerializer(DocumentSerializer):
	class Meta:
		model = Post2
		fields = ('title', 'tags')

class PostDetailSerializer(DocumentSerializer):
	class Meta:
		model = Post2
		fields = ('title', 'author', 'tags', 'comments')

