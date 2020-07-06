# -*- coding: utf-8 -*-

from django.db import models


class Assets(models.Model):
    id = models.AutoField(primary_key=True)
    asset_numbers = models.CharField(max_length=200)  # 资产编号
    use_users = models.CharField(max_length=200)  # 使用人
    department = models.CharField(max_length=200)  # 部门
    brand = models.CharField(max_length=200)  # 品牌
    model = models.CharField(max_length=200)  # 型号
    system_version = models.CharField(max_length=200)  # 系统版本
    resolution = models.CharField(max_length=200)  # 分辨率
    administrator = models.CharField(max_length=200)  # 负责人
    notes = models.CharField(max_length=200)  # 备注
    update_time = models.DateTimeField()  # 最后更新时间
    is_delete = models.IntegerField(default=0)  # 是否被删除
