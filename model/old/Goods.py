#!/usr/bin/env python
# encoding: utf-8
__author__ = 'ethan'

from conf import config
from peewee import *

class Goods(Model):
    id=CharField(primary_key=True)
    sku_id=CharField()
    sku_category_id=CharField()
    sku_category_name=CharField()
    sku_sort_code=CharField()
    sku_name=CharField()
    sku_alias_name=CharField()
    sku_keywords=CharField()
    sku_unit=CharField()
    sku_spec=CharField()
    sku_image_src=CharField()
    sku_image1_src=CharField()
    sku_image2_src=CharField()
    sku_image3_src=CharField()
    supplier_id=CharField()
    supplier_city_id=CharField()
    supplier_city_name=CharField()
    supplier_brand=CharField()
    supplier_image_src=CharField #供应商图标
    unit_price=DecimalField() #销售价格(原价格)
    quantity=IntegerField() #库存数量
    desc=CharField() #商品描述
    count_selled=IntegerField()  #历史销售数量
    is_enable_sell=IntegerField()  #允许销售标志（0：禁止 1：允许）
    remark=TextField() #备注
    create_time=DateTimeField()  #创建时间
    modify_time=DateTimeField()  #最后修改时间
    class Meta:
        database = config.OldDB
        db_table = config.DB_PREFIX + 'goods'

#商品分类
class Category(Model):
    id=CharField() #ID
    name=CharField() #分类名称
    class Meta:
        database = config.OldDB
        db_table = config.DB_PREFIX + 'category'


#区域分类
class City(Model):
    id=CharField()
    name=CharField()
    class Meta:
        database = config.OldDB
        db_table = config.DB_PREFIX + 'city'