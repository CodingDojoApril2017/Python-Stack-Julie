# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django import forms
import bcrypt
import re
import datetime

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
#this is validating any new user
    def validate(self, postData):
        errorStr = []
        if len(postData['name']) < 2:
            errorStr.append("Name field cannot be empty.")

        if len(postData['username']) <2:
            errorStr.append("Username field cannot be empty")
        if User.objects.filter(username=postData['username']):
            errorStr.append("Username is already registered.")

        # if len(postData['birth_date'])< 1:
        #     errorStr.append("Please enter a birthday.")

        if len(postData['email']) < 3:
            errorStr.append("Email field cannot be empty.")
        if not EMAIL_REGEX.match(postData['email']):
            errorStr.append("This is not a valid email address.")
        if User.objects.filter(email=postData['email']):
            errorStr.append("email is already registered.")

        if len(postData["password"]) < 8:
            errorStr.append("Password must be at least 8 characters")
        if postData["password"] != postData["confirmpw"]:
            errorStr.append("Passwords must match each other.")

        encrypted_pw = bcrypt.hashpw(postData["password"].encode(), bcrypt.gensalt())
#This is cthrowing an error if validation fails in anyway
        response_to_views = {}
        if errorStr:
            response_to_views['status'] = False
            response_to_views['errorStr'] = errorStr
#this is creating a new user if they pass all avlidations
        else:
            user = self.create(name = postData["name"], username = postData["username"], email= postData["email"], password = encrypted_pw)
            response_to_views['status'] = True
            response_to_views['userobj'] = user
        return response_to_views
#this is validation for registered User
#userobj is defined in the process section in the views.py section
    def loginUser(self, postData):
        errorStr = []

        user = User.objects.filter(username=postData['username'])
        if not user:
            errorStr.append("Invalid username")
        else:
            if bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()) != user[0].password:
                errorStr.append("Password is incorrect.")
        response_to_views = {}
        if errorStr:
            response_to_views['status'] = False
            response_to_views['errorStr'] = errorStr
        else:
            response_to_views['status'] = True
            response_to_views['userobj'] = user[0]
        return response_to_views

class Thought(models.Model):
    mood= models.TextField(max_length=100)
    think = models.TextField(max_length=255)

class User(models.Model):
    name = models.TextField(max_length=100)
    username = models.TextField(max_length=100)
    email= models.EmailField()
    password = models.TextField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.name
# Create your models here.
