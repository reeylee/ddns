import requests
from lxml import etree
def get_ip(url='https://www.baidu.com/s?wd=ip'):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36", 
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                #"Accept-Encoding":" gzip, deflate, br",
                # "Accept-Language":" zh-CN,zh;q=0.9",
                #"Cache-Control":" max-age=0",
                #"Connection":" keep-alive",
                # "Host": "www.baidu.com",
                # "Sec-Fetch-Site": "none",
                # "Sec-Fetch-User": "?1",
                # "Upgrade-Insecure-Requests": "1",
                
              }
    
    response = requests.get(url,headers=headers)
    #response.encoding='utf-8'
    print(response.text)
    # with open('1.html','wb') as fp:
    #     fp.write(response.text.encode('utf-8'))
    html = etree.HTML(response.text)
    print(response.text)
    content =  html.xpath("//div/table//tr/td/span[@class='c-gap-right']/text()")
    # # content = html.xpath('//div//tr/td/span/a/text()')
    # # print(content)
    try:
        ip = str(content[0]).split(':')[-1]
    except:
        ip = '无法获取ip'
    return ip

if __name__ == "__main__":
    print(get_ip())