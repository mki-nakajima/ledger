# coding: utf-8
'''
Created on 2019/08/07

@author: nakajima

'''

from django.shortcuts import render
from datetime import datetime
from ledger.models.memo import Memo


def index(request):
    # トップ画面表示
    now = datetime.now()
    Memo.objects.create(
        title="タイトル[" + str(Memo.objects.count() + 1) + "]",
        detail=now.strftime("%Y/%m/%d-%H:%M:%S"),
    )
    display_dict = {
        "page_title": now.strftime("%Y/%m/%d %H:%M:%S"),
        "memo_size": Memo.objects.count(),
        "memo": Memo.objects.all(),
    }
#     return HttpResponse("Hello World!!")
    return render(request, 'index.html', display_dict)
