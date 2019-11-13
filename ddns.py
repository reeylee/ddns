 # encoding: utf-8

from getrecord import get_record
from getip import get_ip
from updatedomain import update
from time import sleep
from datetime import datetime
import sys
from constant import OK,FAILD,NOUPDATE


def start_check():
    status={}
    record_list = []
    try:
        _args = sys.argv[1]
        ip = get_ip()
    except:
        _args=None
        ip = None
    else:
        try:
            record = get_record(_args)
            status['code']=OK
            status['msg'] = '获取更新域名成功'
            status['data'] = record
        except:
            status['code'] = FAILD
            status['msg'] = '获取域名信息失败，请检查域名及网络'
            
    if not ip:
        status['code']=FAILD
        status['msg'] = '无法获取ip，请检查网络'
    status['ip'] = ip
    return status

def ddns(ip,record):
    status={
        'date':datetime.now()
    }
    try:
        for r in record:
            if r['Value'] == ip:
                status['code'] = NOUPDATE
                status['msg'] = '不需要更新ip'
                continue
            status = update(r['RecordId'],r['RR'],ip)
            status['date']=datetime.now()
            status.update({'update_domain':r['RR']})
    except:
        status['code'] = FAILD
        status['msg'] = '程序更新失败，请检查网络或程序'

    return status

if __name__ == "__main__":
    start_status = start_check()
    while True:
        if start_status['code']==OK:
            ip = get_ip()
            status = ddns(ip,start_status['data'])
            if status['code'] == OK or status['code']==NOUPDATE:
                print(status)
                start_status = start_check()
                sleep(300)
            else:
                start_status = start_check()
                status = ddns(old_ip,ip,start_status['data'])
                print(status)
                sleep(300)
        else:
            print(status)
            start_status = start_check()
            sleep(300)
