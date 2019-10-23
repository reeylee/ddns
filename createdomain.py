from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
from aliyunsdkalidns.request.v20150109.AddDomainRecordRequest import AddDomainRecordRequest

import sys
sys.path.append("..")
from content import accessKeyId, accessSecret

from getip import get_ip 

client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')

ip=get_ip()
print(type(ip))
request = AddDomainRecordRequest()
request.set_accept_format('json')
request.set_Value(ip)
request.set_Type("A")
request.set_RR("blog")
request.set_DomainName("henqy.club")
response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))
