from mongoengine import *

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    def __str__(self):
    	return self.first_name
