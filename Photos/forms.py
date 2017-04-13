# coding: utf-8

from __future__ import unicode_literals
from django import forms
from Photos.models import Photo

class PhotoEditForm(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ('image_file', 'description', )
#forms jujini to gyumini