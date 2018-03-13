from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Post, Post2, TextPost, LinkPost
from .serializers import PostSerializer, PostCreateSerializer, PostDetailSerializer, PostUpdateSerializer

from rest_framework_mongoengine import viewsets
from rest_framework_mongoengine.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, RetrieveDestroyAPIView, ListAPIView, RetrieveUpdateAPIView
import datetime
#llists: get posts documents in mongodb inserted by api rest
def lists(request):
	for post in Post2.objects:
		print(post.title)
		print(post.author)

	for post in TextPost.objects:
		print(post.content)

	for post in Post2.objects:
		print(post.id, post.title, len(post.title), post.tags)

		if isinstance(post, TextPost):
			print(post.content)

		if isinstance(post, LinkPost):
			print('Link: {}'.format(post.link_url))

	for post in Post2.objects(tags='ssd'):
		print(post.title)

	num_post = Post2.objects(title='Mac').count()
	print(num_post)

	posts = Post2.objects.all()
	return render(request, 'list.html', {'Post': posts})

#index: get all documents in mongodb
def index(request):
	posts = Post.objects
	print(posts)
	return render(request, 'index.html', {'Posts': posts})

# create: create a new post
def create(request):
	if request.method == 'POST':	
		title = request.POST['title']
		content = request.POST['content']

		posts = Post(title=title)
		posts.last_update = datetime.datetime.now() 
		posts.content = content
		posts.save()

	return render(request, 'create.html')

# update: edit post by id, the id was in each document into index function
def update(request):
	id = eval("request." + request.method + "['id']")
	post = Post.objects(id=id)[0]

	if request.method == 'POST':
		post.title = request.POST['title']
		post.last_update = datetime.datetime.now() 
		post.content = request.POST['content']
		post.save()
		template = 'index.html'
		params = {'Posts': Post.objects} 

	elif request.method == 'GET':
		template = 'update.html'
		params = {'post':post}

	return render(request, template, params)

# delete: delete docmuent by id from index function
def delete(request):
	id = eval("request." + request.method + "['id']")

	if request.method == 'POST':
		post = Post.objects(id=id)[0]
		post.delete() 
		template = 'index.html'
		params = {'Posts': Post.objects} 
	elif request.method == 'GET':
		template = 'delete.html'
		params = { 'id': id }

	return render(request, template, params)

class PostListAPIView(ListAPIView):
	queryset = Post2.objects.all()
	serializer_class = PostSerializer

	# def get_queryset(self):
	# 	return Post2.objects.all()
class PostCreateAPIView(CreateAPIView):
	queryset = Post2.objects.all()
	serializer_class = PostCreateSerializer

	def perform_create(self, serializer):
		author = self.request.data['author']
		print("data --->", self.request.data)
		serializer.save(author=author)

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post2.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'id'

class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post2.objects.all()
	serializer_class = PostUpdateSerializer
	lookup_field = 'id'

class PostDeleteAPIView(RetrieveDestroyAPIView):
	queryset = Post2.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'id'

