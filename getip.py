import requests
from lxml import etree
def get_ip(url='https://www.baidu.com/s?wd=ip'):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36", 
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
              }
    
    response = requests.get(url,headers=headers)
    html = etree.HTML(response.text)
    content =  html.xpath("//div/table//tr/td/span[@class='c-gap-right']/text()")
    try:
        ip = str(content[0]).split(':')[-1]
    except:
        ip = '无法获取ip'
    return ip

if __name__ == "__main__":
    print(get_ip())