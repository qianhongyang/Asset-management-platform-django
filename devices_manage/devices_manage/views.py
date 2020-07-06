import operator
from functools import reduce

from django.db.models import Q
from django.http import HttpResponse
import json, time
from .utils import DateEncoder, search_q
from . import models


def add(request):
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
    print(update_time)
    data = {
        "code": 10000,
        "success": True
    }
    if request.method == "POST" or request.method == "post":
        result = json.loads(request.body)
        result['update_time'] = update_time[0]
        models.Assets.objects.create(**result)
        return HttpResponse(json.dumps(data), content_type="application/json,charset=utf-8")
    else:
        return HttpResponse("faild")


def info(request):
    dic = {}
    data = {
        "code": 10000,
        "success": True
    }
    if request.method == "GET" or request.method == "get":
        res_list = json.dumps(list(models.Assets.objects.filter(is_delete=0).values().order_by('-update_time')), cls=DateEncoder)
        dic["assets_info"] = json.loads(res_list)
        return HttpResponse(json.dumps(dic), content_type="application/json,charset=utf-8")
    else:
        return HttpResponse("faild")


def search(request):
    dic = {}
    data = {
        "code": 10000,
        "success": True
    }
    if request.method == "POST" or request.method == "post":
        data = json.loads(request.body)
        for key, value in list(data.items()):
            if value == "" or value is None:
                data.pop(key)
        data["is_delete"] = 0
        search_value = json.dumps(list(models.Assets.objects.filter(**data).values().order_by('-update_time')), cls=DateEncoder)
        dic["assets_info"] = json.loads(search_value)
        return HttpResponse(json.dumps(dic), content_type="application/json,charset=utf-8")
    else:
        return HttpResponse("faild")


def edit(request):
    data = {
        "code": 10000,
        "success": True
    }
    if request.method == "POST" or request.method == "post":
        result = json.loads(request.body)
        asset_id = result.get("id")
        models.Assets.objects.filter(id=asset_id).update(**result)
        print(result)
        return HttpResponse(json.dumps(data), content_type="application/json,charset=utf-8")
    else:
        return HttpResponse("faild")


def delete(request):
    data = {
        "code": 10000,
        "success": True
    }
    if request.method == "POST" or request.method == "post":
        if request.body:
            result = json.loads(request.body)
            asset_id = result
            models.Assets.objects.filter(id=asset_id).update(is_delete=1)
        else:
            result = None
            data = {
                "code": -1,
                "success": False,
                "message": "Error:id is null!"
            }
        return HttpResponse(json.dumps(data), content_type="application/json,charset=utf-8")
    else:
        return HttpResponse("faild")
