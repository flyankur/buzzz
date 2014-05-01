import settings
import datetime
import json
from operator import itemgetter
from django.contrib.auth.models import User
from django.db import models


class Audio(models.Model):
	audio_file_url = models.TextField(default='No Audio File Url ')
	created = models.DateTimeField(auto_now_add=True, editable=False, null=True)