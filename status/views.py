# -*- encoding: utf-8 -*-

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, StreamingHttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.generic import ListView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from contact.models import *
