from mongoengine import *
from blog.settings import DBNAME
from users.models import User

connect(DBNAME)

class Comment(EmbeddedDocument):
	content = StringField()
	name = StringField(max_length=120)

class Post(Document):
	# _id = StringField()
	title = StringField(max_length=120, required=True)
	content = StringField(max_length=500, required=True)
	last_update = DateTimeField()

	def __str__(self):
		return self.title

class Post2(Document):
	title = StringField(max_length=120, required=True)
	author = ReferenceField(User, reverse_delete_rule=CASCADE)
	tags = ListField(StringField(max_length=30))

	comments = ListField(EmbeddedDocumentField(Comment))
	meta = {'allow_inheritance': True}

	def __str__(self):
		return self.title

class TextPost(Post2):
	content = StringField()

class ImagePost(Post2):
	image_path = StringField()

class LinkPost(Post2):
	link_url = StringField()

class UserPost(Document):
	title = StringField(max_length=50, required=True)
	author = ReferenceField(User, reverse_delete_rule=CASCADE)

class PostReview(Document):
	content = StringField(max_length=50, required=True)
	post = ReferenceField(UserPost, reverse_delete_rule=CASCADE)

	class Meta:
		verbose_name = 'PostReview'
		verbose_name_plural = 'PostReviews'