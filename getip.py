import requests
from lxml import etree
def get_ip(url='https://www.ipip.net/ip/'):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36" }
    response = requests.get(url,headers=headers)
    response.encoding='utf-8'
    # with open('1.html','wb') as fp:
    #     fp.write(response.text.encode('utf-8'))
    html = etree.HTML(response.text)
    # content =  html.xpath("//div/table//tr/td/span[@class='c-gap-right']/text()")
    content = html.xpath('//div//tr/td/span/a/text()')
    # print(content)
    try:
        ip = str(content[0]).split(':')[-1]
    except:
        ip = '无法获取ip'
    return ip

if __name__ == "__main__":
    print(get_ip())