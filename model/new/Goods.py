#!/usr/bin/env python
# encoding: utf-8
__author__ = 'ethan'

from conf import config
from peewee import *
import time

#商品表
class Goods(Model):
    goods_id=IntegerField(primary_key=True,sequence=True) #商品ID
    category_id=IntegerField() #类别ID
    supplier_id=IntegerField() #商户ID
    city=CharField() #城市
    goods_name=CharField() #商品名称
    image=CharField() #商品封面图
    spec=CharField() #规格
    unit=CharField() #单位
    unit_price=FloatField() #单价
    quantity=CharField() #库存数量
    total_sell=CharField() #历史销售量	批量更新
    score=CharField() #评分	批量更新
    description=TextField() #描述
    status=IntegerField() #状态值	"0:逻辑删除 1:待审核，商家可修改 default 2:可销售 3:冻结中，商家不可修改"
    is_promotion=IntegerField() #是否促销
    insert_time=IntegerField(default=int(time.time())) #插入时间
    modify_time=IntegerField(default=int(time.time())) #更新时间
    class Meta:
        database = config.NewDB
        db_table = config.DB_PREFIX + 'goods'

#商品分类
class Category(Model):
    category_id=IntegerField(primary_key=True,sequence=True) #ID
    category_name=CharField() #分类名称
    fid=IntegerField(default=0)
    sort_code=IntegerField(default=9999)
    insert_time=IntegerField(default=int(time.time())) #插入时间
    modify_time=IntegerField(default=int(time.time())) #更新时间
    class Meta:
        database = config.NewDB
        db_table = config.DB_PREFIX + 'category'
