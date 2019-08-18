# -*- coding: utf-8 -*-
'''
Created on 2019/08/18

@author: Nakajima

抽象クラス
単体では使用しない
色々なテーブルに共通の、作成日時・更新日時・更新ユーザIDを持つテーブル
'''
from django.db import models
from datetime import datetime


# 抽象モデルクラス
class AbstractUpdateCommon(models.Model):
    # 作成日時
    created_at = models.DateTimeField(default=datetime.now,\
                                      verbose_name=u'作成日時')
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True,\
                                      verbose_name=u'更新日時')
    # 更新ユーザーID
    mod_user_id = models.IntegerField(null=False,\
                                      default=1,\
                                      editable=False,\
                                      verbose_name=u'更新ユーザーID')

    class Meta:
        app_label = 'ledger'
        abstract = True
