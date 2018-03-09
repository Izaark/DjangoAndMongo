from django.shortcuts import render
from posts.models import Post2, TextPost, LinkPost


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


