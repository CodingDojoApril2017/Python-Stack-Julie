# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . models import Users, UserManager
from django.contrib import messages



#this is the index
def index(request):
	return render(request, "first_app/index.html")

#this is the redirect route for the form"create"
#the validation works but the success page does not get displayed
def create(request):
	user = Users.objects.validateUsername(request.POST)
	if user[0] == True:
		messages.success(request, request.POST['username'])
		return redirect("/success")
	else:
		for i in user[1]:
			messages.error(request, i)
	return redirect("/")

#this is the success page
def success(request):
    context = {
        "users": Users.objects.all()
    }
    return render(request, "first_app/success.html", context)
# Create your views here.
