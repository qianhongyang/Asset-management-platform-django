# coding=utf-8
import datetime
import json


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


def search_q(data):
    list_a = []
    for key, value in list(data.items()):
        a = key + "__contains"
        c = "Q( %s= '%s')" % (a, value)
        list_a.append(c)
    res = "|".join(list_a)
    return res

