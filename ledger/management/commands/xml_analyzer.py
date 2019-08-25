# -*- coding: utf-8 -*-
'''
Created on 2019/08/25

機能名：XML解析機能
概要：複数の子タグを持つタグ名を指定し、その子タグの値を取得する

@author: shunsuke
'''
import sys
import re
import traceback
from xml.etree.ElementTree import parse
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

# メインメソッドの引数の数
MAIN_ARGS_LENGTH = 3

# ログメッセージ用の関数名など
FUNC_NAME = "ckdb_report_creator"
LOG_MSG_CONFIRMATION_TAG_EXISTENCE = "Unification tag existence confirmation: "
LOG_MSG_CONFIRMATION_TAG_VALUE = "Unification tag value confirmation: "
LOG_MSG_OK = "OK"
LOG_MSG_NG = "NG"
LOG_MSG_CANNOT_AUTO_FIX = "Cannot auto fix the tag not allowed blank."
LOG_MSG_TAG_CREATE = "Create element: "
LOG_MSG_TAG_APPEND = "Append element: "
LOG_MSG_TAG_DELETE = "Delete parent_element: "


def analyze_xml(first_xml, second_xml, xml_config):
    '''
    2つのXMLを設定に基づいて解析する

    処理内容
    2つのXMLを設定に基づいて解析する
    @param string  読み込むXMLファイル1のパス
    @param string  読み込むXMLファイル2のパス
    @param object 読み込み設定（辞書式）
    '''
    # XMLファイル読込
    first_xml_file = None
    second_xml_file = None
    try:
        first_xml_file = parse(first_xml)
        second_xml_file = parse(second_xml)
    except Exception:
        print("XML Parse Error.")
        print("First:", first_xml)
        print("Second:", second_xml)
        return

    for conf in xml_config:
        type_name =conf.get("type_name", "blank")
        if type_name == "blank":
            continue
        print("analyze:", type_name)
        if type_name == "type_1":
            analyze_type_1(first_xml_file, second_xml_file, conf)
        elif type_name == "type_2":
            pass
        elif type_name == "type_3":
            pass
        else:
            print("No expeceted type_name:", type_name)


def analyze_type_1(first_xml_file, second_xml_file, conf):
    first_root_element = first_xml_file.getroot()
    second_root_element = second_xml_file.getroot()

    first_conf = conf.get("first", {})
    second_conf = conf.get("second", {})

    # analyze first
    parent_tag_name = first_conf.get("parent_tag_name", "")
    child_tag_name = first_conf.get("child_tag_name", "")
    child_tag_attrs = first_conf.get("child_tag_attrs", [])

    parent_tag = first_root_element.find(parent_tag_name)
    for child_tag in parent_tag.findall(child_tag_name):
        for attr_name in child_tag_attrs:
            print(child_tag.get(attr_name))

    parent_tag_name = second_conf.get("parent_tag_name", "")
    child_tag_name = second_conf.get("child_tag_name", "")
    grand_child_tag_names = second_conf.get("grand_child_tag_names", [])
    for parent_tag in second_root_element.findall(parent_tag_name):
        # 特定のタグの値が、想定のものかチェックする
        for child_tag in parent_tag.findall(child_tag_name):
            for grand_child_tag in grand_child_tag_names:
                print(child_tag.find(grand_child_tag).text)

if __name__ == '__main__':
    # 引数の数チェック
    if len(sys.argv) < MAIN_ARGS_LENGTH:
        print("引数には、XMLファイルパス1、XMLファイルパス2が必要です。")
        sys.exit(-1)

    first_xml_file = sys.argv[1]
    second_xml_file = sys.argv[2]

    # 読み込むタグなどの設定
    xml_analyze_config = [
        {
            "type_name": "type_name",
            "first": {
                "parent_tag_name": "tag_name_1",
                "child_tag_name": "tag_1",
                "child_tag_attrs": [
                    "attr_1",
                    "attr_2",
                    "attr_3",
                ],
            },
            "second": {
                "parent_tag_name": "tag_name_1",
                "child_tag_name": "tag_1",
                "grand_child_tag_names": [
                    "tag_1",
                    "tag_2",
                    "tag_3",
                ],
            },
        },
        {
            "type_name": "type_name",
            "first": {
                "parent_tag_name": "tag_name_1",
                "child_tag_name": "tag_1",
                "child_tag_attrs": [
                    "attr_1",
                    "attr_2",
                    "attr_3",
                ],
            },
            "second": {
                "parent_tag_name": "tag_name_1",
                "child_tag_name": "tag_1",
                "grand_child_tag_names": [
                    "tag_1",
                    "tag_2",
                    "tag_3",
                ],
            },
        },
        {
            "type_name": "type_name",
            "first": {
                "parent_tag_name": "tag_name_2",
                "child_tag_name": "tag_2",
                "child_tag_attrs": [
                    "attr_1",
                    "attr_2",
                    "attr_3",
                ],
            },
            "second": {
                "parent_tag_name": "tag_name_3",
                "child_tag_name": "tag_3",
                "grand_child_tag_names": [
                    "tag_1",
                    "tag_2",
                    "tag_3",
                ],
            },
        },
    ]

    try:
        analyze_xml(first_xml_file, second_xml_file, xml_analyze_config)
    except Exception:
        print(traceback.format_exc())