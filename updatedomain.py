from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest

from content import accessKeyId, accessSecret

from getip import get_ip 
def update(record_id,ip):
    client = AcsClient(accessKeyId, accessSecret, 'cn-hangzhou')

    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')

    
    request.set_RecordId(record_id)
    request.set_RR("blog")
    request.set_Type("A")
    request.set_Value(ip)

    try:
        response = client.do_action_with_exception(request)
        return {'code':0,'msg':'update ok'}
    except:
        return {'code':1,'msg':'update fail'}

if __name__ == "__main__":

    ip = str(get_ip())

    print(len(record_id),len(ip))
    
    update(record_id,ip)
