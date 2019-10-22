#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest

from content import accessSecret, accessKeyId
def getrecordid():

    client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')

    request = DescribeDomainRecordsRequest()
    request.set_accept_format('json')

    request.set_DomainName("henqy.club")
    request.set_RRKeyWord("ddns")
    response = client.do_action_with_exception(request)
    return response
# python2:  print(response) 
if __name__ == "__main__":
    response = getrecordid()
    print(str(response, encoding='utf-8'))

