from django.shortcuts import render, get_object_or_404

from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Post
import datetime

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

