#!/usr/bin/env python
# encoding: utf-8
__author__ = 'ethan'

from peewee import *

#OldDB = MySQLDatabase(host='127.0.0.1', user='root', passwd='root', database='chddv4', port=3306)
OldDB = MySQLDatabase(host='192.168.1.7', user='root', passwd='chdd1234', database='chddv4', port=3306)
#NewDB = MySQLDatabase(host='127.0.0.1', user='root', passwd='root', database='chddv5', port=3306)
NewDB = MySQLDatabase(host='192.168.1.7', user='root', passwd='chdd1234', database='chddv5', port=3306)

DB_PREFIX = 't_'