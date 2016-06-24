#!/usr/bin/env python
# encoding: utf-8
__author__ = 'ethan'

import datetime, time


# Datetime转化为TimeStamp
def datetime2timestamp(dt, convert_to_utc=False):
    ''' Converts a datetime object to UNIX timestamp in milliseconds. '''
    if isinstance(dt, datetime.datetime):
        if convert_to_utc:  # 是否转化为UTC时间
            dt = dt + datetime.timedelta(hours=-8)  # 中国默认时区
        timestamp = int((dt - datetime.datetime(1970, 1, 1)).total_seconds())
        return timestamp
    return dt


# TimeStamp转化为Datetime
def timestamp2datetime(timestamp, convert_to_local=False):
    ''' Converts UNIX timestamp to a datetime object. '''
    if isinstance(timestamp, (int, long, float)):
        dt = datetime.datetime.utcfromtimestamp(timestamp)
        if convert_to_local:  # 是否转化为本地时间
            dt = dt + datetime.timedelta(hours=8)  # 中国默认时区
        return dt
    return timestamp


# 当前UTC时间的TimeStamp
def timestamp_utc_now():
    return datetime2timestamp(datetime.datetime.utcnow())


# 当前本地时间戳
def timestamp_now():
    return datetime2timestamp(datetime.datetime.now())



def MobileFormat(string):
    return string if string.find('') < 0 else (
            ','.join(string.split()) if string.find('/') < 0 else ','.join(string.split('/')))