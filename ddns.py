 # encoding: utf-8
 
from getrecord import get_record
from getip import get_ip
from updatedomain import update
from time import sleep
def choice_domain():
    record = get_record()
    i = 0
    print('您的域名有：')
    for items in record:
        print('{}:{}.{}'.format(i,items['RR'],items['DomainName']))
        i += 1
    index = input('请输入您要更新的域名序号：')
    ip = get_ip()
    try:
        index = int(index)
        if index <= i and index >= 0:
            if ip == record[index]['Value']:
                return {'code':0,'msg':'不需要更新'}
            record_id = record[index]['RecordId']
            rr = record[index]['RR']
            return {'code':2,'data':(record_id,rr,ip)}
        else:
            print('您输入的有误，请重新输入')
            choice_domain()
    except:
        print('您输入的有误，请重新输入')
        choice_domain()
    
def ddns(choice_domain):
    try:
        info = choice_domain()
        if info['code'] == 0:
            return info
        elif info['code'] == 2:
            print(info)
            status = update(info['data'][0],info['data'][1],info['data'][2])
        return status
    except:
        return {'code':1,'msg':'更新失败'}

if __name__ == "__main__":
    status = ddns(choice_domain)
    while True:
        if status['code'] == 0:
            print(status)
            sleep(300)      
        else:
            print(status)
            status=ddns(choice_domain)
            sleep(10)