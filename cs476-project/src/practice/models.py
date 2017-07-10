# -*- coding: utf-8 -*-
# This is how we are going to store data in the database

from __future__ import unicode_literals

from django.db import models

import os
# Create your models here.

class Manager(models.Manager):
	def add(self, model, filename, chapter):
		location = "data/" + filename
		path = os.path.join(os.path.dirname(__file__), location)

		file = open(path, 'r')

		for line in file:
			line = unicode(line,"UTF-8")
			jap = line.split(":")[0].strip()
			eng = line.split(":")[1].strip()

			temp = None
			exists = None
			if model == "hiragana":
				temp = Hiragana()
				exists = Hiragana.objects.filter(japanese=jap).exists()
			elif model == "katakana":
				temp = Katakana()
				exists = Katakana.objects.filter(japanese=jap).exists()
			elif model == "vocab":
				temp = Vocab()
				temp.chapter = chapter
				exists = Vocab.objects.filter(japanese=jap).exists()
			elif model == "kanji":
				temp = Kanji()
				temp.chapter = chapter
				exists = Kanji.objects.filter(japanese=jap).exists()

			if not(exists):
				temp.japanese = jap
				temp.english = eng
				temp.save()


class Hiragana(models.Model):
	japanese = models.CharField(max_length=3)
	english = models.CharField(max_length=3)


class Katakana(models.Model):
	japanese = models.CharField(max_length=3)
	english = models.CharField(max_length=3)

class Vocab(models.Model):
	japanese = models.CharField(max_length=10)
	english = models.CharField(max_length=10)
	chapter = models.IntegerField()

class Kanji(models.Model):
	japanese = models.CharField(max_length=10)
	english = models.CharField(max_length=10)
	chapter = models.IntegerField()


