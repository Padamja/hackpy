# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserProfileManager(BaseUserManager):
	def create_user(self, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			username=username,
			)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, username, password):
		user = self.create_user(password=password,
								username=username,
								)
		user.save(using=self._db)
		user.is_admin = True
		return user

class UserProfile(models.Model):
	username = models.CharField(max_length=200)
	is_admin = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
																																																																																																																																																																																																																																																																																																																																																		