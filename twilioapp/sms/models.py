from django.db import models

# Create your models here.

class Contacts(models.Model):
	friend_name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=10)

	def __unicode__(self):
		return self.friend_name

	def get_phone_number(self):
		return self.phone_number