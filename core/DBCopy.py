#!/usr/bin/env python
# encoding: utf-8
__author__ = 'ethan'

import sys, time
from core.Common import *
from model.new import Goods as newGoods
from model.new import User as newUser
from model.old import Goods as oldGoods
from model.old import User as oldUser
from tornado import log


class DBCopy():
    def __init__(self):
        self.citydict = dict()
        for city in oldGoods.City.select():
            self.citydict[city.id] = city.name

        for category in oldGoods.Category.select():
            newCategory = {
                'category_id': category.id,
                'category_name': category.name
            }
            newGoods.Category.create(**newCategory)

        for customer in oldUser.Customer.select():
            newCustomer = self.AddNewCustomer(customer)
            self.AddAddress(customer, newCustomer.customer_id)


        i = 1
        while (i):
            if oldUser.Supplier.select().paginate(i, 100).count() == 0:
                break
            print oldUser.Supplier.select().count()
            for supplier in oldUser.Supplier.select():
                newSupplier = self.AddNewSupplier(supplier)
                log.app_log.info('supplier_id %i' % newSupplier.supplier_id)
                for item in oldGoods.Goods.select().where(oldGoods.Goods.supplier_id == supplier.id):
                    pic_group = []
                    if item.sku_image_src not in ['', None]: pic_group.append(item.sku_image_src.replace('\\','/'))
                    if item.sku_image1_src not in ['', None]: pic_group.append(item.sku_image1_src.replace('\\','/'))
                    if item.sku_image2_src not in ['', None]: pic_group.append(item.sku_image2_src.replace('\\','/'))
                    if item.sku_image3_src not in ['', None]: pic_group.append(item.sku_image3_src.replace('\\','/'))
                    item.imagegroup = ','.join(pic_group)
                    self.AddNewGoods(item, newSupplier.supplier_id)
            i = i + 1
            log.app_log.info(i)

    def AddNewCustomer(self, item):
        try:
            newCustomer = dict()
            newCustomer['account'] = item.account
            newCustomer['password'] = item.password
            newCustomer['type'] = 1
            newCustomer['customer_name'] = item.contact_name
            newCustomer['head_image'] = item.head_image_src or ''
            newCustomer['city'] = item.city_name
            newCustomer['is_enable_login'] = item.is_enable_login
            newCustomer['is_enable_pay_offline'] = item.is_allow_pay_offline
            newCustomer['insert_time'] = datetime2timestamp(item.create_time)
            newCustomer['modify_time'] = datetime2timestamp(item.modify_time) or int(time.time())
            newCustomer['last_login_time'] = newCustomer['modify_time']
            return newUser.Customer.create(**newCustomer)
        except Exception, exception:
            print self.newCustomer, item.id
            log.app_log.error('error %s' % exception.args)

    def AddAddress(self, item, cid):
        try:
            tempItem = dict()
            tempItem['customer_id'] = cid
            tempItem['city'] = item.city_name
            tempItem['address'] = item.address
            tempItem['contact_name'] = item.contact_name
            tempItem['mobile'] = MobileFormat(item.mobile)
            tempItem['route'] = item.route
            return newUser.Address.create(**tempItem)
        except Exception, exception:
            print tempItem, item.id
            log.app_log.error('error %s' % exception.args)

    def AddNewSupplier(self, item):
        try:
            newSupplier = dict()
            newSupplier['account'] = item.account
            newSupplier['password'] = item.password
            newSupplier['city'] = item.city_name
            newSupplier['brand'] = item.brand
            newSupplier['logo'] = item.image_src.replace('\\','/')
            newSupplier['contact_name'] = item.contact_name
            newSupplier['mobile'] = MobileFormat(item.mobile)
            newSupplier['address'] = item.address
            newSupplier['open_time'] = item.open_time
            newSupplier['close_time'] = item.close_time
            newSupplier['score'] = item.score
            newSupplier['is_enable_login'] = item.is_enable_login
            newSupplier['insert_time'] = datetime2timestamp(item.create_time)
            newSupplier['modify_time'] = datetime2timestamp(item.modify_time) or int(time.time())
            newSupplier['last_login_time'] = newSupplier['modify_time']
            return newUser.Supplier.create(**newSupplier)
        except Exception, exception:
            print newSupplier, item.id
            log.app_log.error('error %s' % exception.args)

    def AddNewGoods(self, item, sid):
        try:
            newGoodsitem = dict()
            newGoodsitem['category_id'] = int(item.sku_category_id)
            newGoodsitem['supplier_id'] = sid
            newGoodsitem['city'] = self.citydict[item.supplier_city_id] if item.supplier_city_id not in ['',
                                                                                                         None] else ''
            newGoodsitem['goods_name'] = item.sku_name
            newGoodsitem['image'] = item.imagegroup
            newGoodsitem['spec'] = item.sku_spec
            newGoodsitem['unit'] = item.sku_unit
            newGoodsitem['unit_price'] = float(item.unit_price)
            newGoodsitem['quantity'] = item.quantity
            newGoodsitem['total_sell'] = item.count_selled
            newGoodsitem['score'] = 5
            newGoodsitem['description'] = item.desc or ''
            newGoodsitem['status'] = 2 if item.is_enable_sell == 1 else 1
            newGoodsitem['is_promotion'] = 0
            newGoodsitem['insert_time'] = datetime2timestamp(item.create_time)
            newGoodsitem['modify_time'] = datetime2timestamp(item.modify_time) or int(time.time())
            return newGoods.Goods.create(**newGoodsitem)
        except Exception, exception:
            print newGoodsitem, item.id
            log.app_log.error('error %s' % exception.args)


if __name__ == '__main__':
    from tornado import options

    options.options.logging = "debug"
    options.parse_command_line()
    DBCopy()
