from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, StreamingHttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.generic import ListView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from django.shortcuts import render
from configovn.models import *
# Create your views here.

logger = logging.getLogger(__name__)


def json_iterator(data=None, pkname=None):
    for d in json.loads(data):
        fields = d[u'fields']
        fields[pkname] = d[u'pk']
        for f in fields:
            if fields[f] == None:
                fields[f] = u"None"
        yield fields


@login_required(login_url='/login/')
def GroupsView(request):
    if request.method == 'GET':
        data = serializers.serialize("json", ConfigsAdvanced.objects.all())
        #  response = StreamingHttpResponse(json_iterator(data), 'contect_typ')
        #  response['Content-Type'] = 'application/json'
        return StreamingHttpResponse(
            json_iterator(data),
            content_type="application/json")
    # return StreamingHttpResponse(json.dumps(data, ensure_ascii=True), content_type="application/json")
