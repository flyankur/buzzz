import json
import time
import os
from datetime import datetime
from operator import itemgetter
import logging
import urllib
import HTMLParser

from django.http import (HttpResponse, HttpResponseRedirect)
from django.core.context_processors import csrf
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

import settings

from hashlib import md5
from django import forms

from buzzz.models import *

from django.views.decorators.http import require_POST

import requests

def render_json(response_dict):
    result = json.dumps(response_dict)
    response = HttpResponse(result)
    response['Content-Type'] = 'application/json'
    response['Content-Length'] = len(result)
    return response

@csrf_exempt
def recorded(request):
    try:
        import pdb; pdb.set_trace()
        audio_file_url = request.POST['audio_file_url']
        audio = Audio.objects.create(audio_file_url=audio_file_url)
        audio.save()
        return render_json({'success': True, 'message': 'Audio file Processing'})
    except Exception as inst:
        return render_json({'success': False, 'message': 'Save failed'})