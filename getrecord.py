#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from json import loads,dumps,load,dump
from content import accessSecret, accessKeyId
def get_record():

    client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')

    request = DescribeDomainRecordsRequest()
    request.set_accept_format('json')

    request.set_DomainName("henqy.club")
    #request.set_RRKeyWord(rr)
    response = client.do_action_with_exception(request)
    record = loads(response)['DomainRecords']['Record']
    return record
# python2:  print(response) 
if __name__ == "__main__":
    record = get_record('blog')
    print(record)

