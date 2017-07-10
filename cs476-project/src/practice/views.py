# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import *
import jsonpickle

#All the valuable information for CSS is inside of bootstrap-3.3.7/dist/css/bootstrap.css
#We can modify the code to create it our own and figure out what we want to do with it.

# Create your views here.
def Home(request):
	context = {}
	return render(request, "practice/home.html", context)

def Study(request, t="hiragana"):
	data = []
	qs = None
	context = {}

	if (t == "hiragana"):
		qs = Hiragana.objects.all()
	elif (t == "katakana"):
		qs = Katakana.objects.all()
	elif (t == "vocab"):
		qs = Vocab.objects.all()
	elif (t == "kanji"):
		qs = Kanji.objects.all()


	for q in qs:
		data.append([q.japanese, q.english])

	
	context["data"] = jsonpickle.encode(data)
	return render(request, "practice/study.html", context)

def Categories(request):
	return render(request, "practice/categories.html", {})