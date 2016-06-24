#!/usr/bin/env python
# encoding: utf-8
__author__ = 'ethan'

from conf import config
from peewee import *

#客户表
class Customer(Model):
    id=CharField()
    account=CharField()
    password=CharField()
    city_id=CharField()
    city_name=CharField()
    brand=CharField()
    contact_name=CharField()
    mobile=CharField()
    address=CharField()
    route=CharField()
    is_enable_login=IntegerField()
    remark=TextField()
    wechat_open_id=CharField()
    head_image_src=CharField()
    create_time=DateTimeField()
    modify_time=DateTimeField()
    is_allow_pay_offline=IntegerField()
    class Meta:
        database = config.OldDB
        db_table = config.DB_PREFIX + 'customer'


#客户配送单
class CustomerGoods(Model):
    id=IntegerField(primary_key=True)
    create_time=IntegerField()
    city_id=CharField()
    city_name=CharField()
    admin_id=CharField()
    admin_name=CharField()
    class Meta:
        database = config.OldDB
        db_table = config.DB_PREFIX + 'customer_goods'


#供应商
class Supplier(Model):
    id=CharField(primary_key=True)
    account=CharField()  #登录名（默认为手机号）
    password=CharField()  #登录密码
    city_id=CharField()  #城市ID
    city_name=CharField()  #城市
    brand=CharField()  #店名
    image_src=CharField()  #图标
    contact_name=CharField()  #联系人
    mobile=CharField()  #联系电话
    address=CharField()  #地址
    score=FloatField(default=0.0) #评分
    is_enable_login=CharField(default='1') #允许登录标志（0禁止1允许）
    remark=TextField() #备注信息
    create_time=DateTimeField()  #创建时间
    modify_time=DateTimeField()  #最后修改时间
    open_time=TimeField()  #开业时间
    close_time=TimeField()  #结业时间
    class Meta:
        database = config.OldDB
        db_table = config.DB_PREFIX + 'supplier'


#供应商商品
class SupplierGoods(Model):
    id=IntegerField(primary_key=True) #ID
    supplier_id=CharField() #供应商ID
    supplier_city_id=CharField() #供应商城市ID
    supplier_city_name=CharField() #供应商城市名
    supplier_brand=CharField() #供应商店铺
    create_time=DateTimeField() #创建时间
    is_signed=CharField() #是否签收
    quantity_subtotal=IntegerField() #数量总计
    price_subtotal=DecimalField() #价格总计
    class Meta:
        database = config.OldDB
        db_table = config.DB_PREFIX + 'supplier_goods'