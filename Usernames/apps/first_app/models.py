# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#this is where the validations take place
class UserManager(models.Manager):
    def validateUsername(self, postData):
        validation_errors =[]
        if len(postData['username']) < 8:
            validation_errors.append('This is too short')
        if len(postData['username']) > 16:
            validation_errors.append('This is too long')
#you can also replace Users.OBjects part with 'self.create'
        if len(validation_errors) == 0:
            C = Users.objects.create(username = request.POST['username'])
            return (True, C)
        else:
            return (False, validation_errors)
        # print postData

#this is the database
class Users(models.Model):
    username = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
