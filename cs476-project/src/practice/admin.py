# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
# Register your models here.


class HiraganaModelAdmin(admin.ModelAdmin):
	list_display = ['japanese', 'english']
	class Meta:
		model = Hiragana

class KatakanaModelAdmin(admin.ModelAdmin):
	list_display = ['japanese', 'english']
	class Meta:
		model = Katakana

class VocabModelAdmin(admin.ModelAdmin):
	list_display = ['japanese', 'english', 'chapter']
	class Meta:
		model = Vocab

class KanjiModelAdmin(admin.ModelAdmin):
	list_display = ['japanese', 'english', 'chapter']
	class Meta:
		model = Kanji

admin.site.register(Hiragana, HiraganaModelAdmin)
admin.site.register(Katakana, KatakanaModelAdmin)
admin.site.register(Vocab, VocabModelAdmin)
admin.site.register(Kanji, KanjiModelAdmin)