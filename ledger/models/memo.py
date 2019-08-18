# -*- coding: utf-8 -*-
'''
Created on 2019/08/18

@author: Nakajima

メモテーブル
メモした情報を持つテーブル
'''
from django.db import models
from ledger.models.abstract_update_common import AbstractUpdateCommon

# メモテーブル
class Memo(AbstractUpdateCommon):
    # タイトル
    title = models.CharField(\
      max_length=100,\
      default='',\
      verbose_name=u'内容',\
    )
    # 内容
    detail = models.CharField(\
      max_length=300,\
      default='',\
      verbose_name=u'内容',\
    )

    class Meta:
        app_label = 'ledger'

    def __unicode__(self):
        return self.title
