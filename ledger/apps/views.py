# coding: utf-8
'''
Created on 2019/08/07

@author: nakajima

'''

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime


def index(request):
    # トップ画面表示
    now = datetime.now()
    display_dict = {
        "title": now.strftime("%Y/%m/%d %H:%M:%S"),
    }
    return HttpResponse("Hi Django~!!")
#     return render_to_response('index.html',
#                               display_dict,
#                               context_instance=RequestContext(request))
