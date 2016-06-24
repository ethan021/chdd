#!/usr/bin/env python
# encoding: utf-8
__author__ = 'ethan'

from conf import config
from peewee import *
import time

#客户
class Customer(Model):
    customer_id=IntegerField(primary_key=True,sequence=True) #客户ID
    account=CharField() #登陆名
    password=CharField() #密码MD5
    type=IntegerField() #类型
    customer_name=CharField() #花店:花店名  个人:昵称
    head_image=CharField() #头像
    city=CharField() #城市
    is_enable_login=IntegerField() #是否允许登陆
    is_enable_pay_offline=IntegerField() #是否允许货到付款
    last_login_ip=CharField() #最后登陆IP
    last_login_time=IntegerField() #最后登陆时间
    insert_time=IntegerField(default=int(time.time())) #插入时间
    modify_time=IntegerField(default=int(time.time())) #更新时间
    class Meta:
        database = config.NewDB
        db_table = config.DB_PREFIX + 'customer'

#供应商
class Supplier(Model):
    supplier_id=IntegerField(primary_key=True,sequence=True) #商家ID
    account=CharField() #登陆名
    password=CharField() #密码
    city=CharField() #城市
    brand=CharField() #店铺名
    logo=CharField() #店铺logo
    contact_name=CharField() #联系人
    mobile=CharField() #手机
    address=CharField() #商家地址
    open_time=TimeField() #开店时间
    close_time=TimeField() #关店时间
    score=FloatField() #商家评分
    is_enable_login=IntegerField(default=1) #是否允许登陆
    last_login_ip=CharField() #最后登陆IP
    last_login_time=IntegerField() #最后登陆时间
    insert_time=IntegerField(default=int(time.time())) #插入时间
    modify_time=IntegerField(default=int(time.time())) #更新时间
    class Meta:
        database = config.NewDB
        db_table = config.DB_PREFIX + 'supplier'

#客户地址
class Address(Model):
    customer_address_id=PrimaryKeyField()
    customer_id=IntegerField()
    city=CharField()
    address=CharField()
    contact_name=CharField()
    mobile=CharField()
    route=CharField()
    is_active=IntegerField(default=1)
    insert_time=IntegerField(default=int(time.time())) #插入时间
    modify_time=IntegerField(default=int(time.time())) #更新时间
    class Meta:
        database = config.NewDB
        db_table = config.DB_PREFIX + 'customer_address'
