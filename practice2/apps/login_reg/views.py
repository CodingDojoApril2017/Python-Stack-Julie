# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Thought
from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
# from .models import Mood

def index(request):
    return render(request, "login_reg/index.html")

#this is the "process" for validation
def process(request, route):
	if request.method == "POST":
		# this brings in the value of response_to_views
		if route == "register":
			response_from_models = User.objects.validate(request.POST)
		else:
			response_from_models = User.objects.loginUser(request.POST)
		if not response_from_models["status"]:
			for error in response_from_models["errorStr"]:
				messages.error(request, error)
			return redirect("login_reg:index")
	request.session["user_id"] = response_from_models["userobj"].id
	print request.session["user_id"]
	return redirect("login_reg:success")
#remember to change the redirect when you add the second app if there are no errors
def success(request):
    bloop = {
        'bloop':Thought.objects.all(),
    }
    return render(request, "login_reg/success.html", bloop)

#this is to fill in the table, the table's actio is opinionof user's thoughts
def opinion( request):
    if request.method == 'POST':
        print request.POST
        Thought.objects.create(mood = request.POST['mood'], think=request.POST['think'])
    return redirect("login_reg:success")




# Create your views here.
