 # encoding: utf-8

from getrecord import get_record
from getip import get_ip
from updatedomain import update
from time import sleep
# def ():
#     record = get_record()
#     i = 0
#     print('您的域名有：')
#     for items in record:
#         print('{}:{}.{}'.format(i,items['RR'],items['DomainName']))
#         i += 1
#     index = input('请输入您要更新的域名序号：')
#     ip = get_ip()
#     try:
#         index = int(index)
#         if index <= i and index >= 0:
#             # if ip == record[index]['Value']:
#             #     return {'code':0,'msg':'不需要更新'}
#             record_id = record[index]['RecordId']
#             rr = record[index]['RR']
#             return {'code':2,'data':(record_id,rr,ip)}
#         else:
#             print('您输入的有误，请重新输入')
#             choice_domain()
#     except:
#         print('您输入的有误，请重新输入')
#         choice_domain()
import sys
try:
    _args = sys.argv[1]
except:
    _args=None
def ddns(_args=_args):
    try:
        ip = get_ip()
        if _args:
            record = get_record(rr=_args)
        else:
            record = get_record()
        if record :
            domain=[]
            for r in record:
                domain.append(r['RR'])
                if ip == r['Value']:
                    status = {
                        'code':0,
                        'msg':'域名：%s不需要更新'%str(domain)
                    }
                    continue 
                status = update(r['RecordId'],r['RR'],ip)
            return status
    except:
        return {'code':1,'msg':'更新失败'}

if __name__ == "__main__":
    status = ddns()
    while True:
        if status['code'] == 0:
            print(status)
            sleep(300)      
        else:
            print(status)
            status=ddns()
            sleep(10)