"""
    通用方法
"""

import requests #
import socket #
import re #

from loguru import logger #

# 获取外网IP
def get_out_ip(timeout=1, method=0):
    out_ip = None 

    if method == 0:
        out_ip = requests.get('http://ifconfig.me/ip', timeout=timeout).text.strip()
    
    elif method == 1:
        out_ip = requests.get('https://checkip.amazonaws.com', timeout=timeout).text.strip()
    
    elif method == 2:
        out_ip = requests.get('http://ipv4.icanhazip.com/', timeout=timeout).text.strip()

    elif method == 3:
        headers = { 
                'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            }
        html_text = requests.get("http://checkip.dyndns.org/", headers=headers, timeout=timeout)
        grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', html_text.text)
        out_ip = grab[0]
    else:
        assert AssertionError("method error")

    return out_ip

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip

def get_host_iplist(domain:str):
    # 获取域名解析出的IP列表
    ip_list = []
    try:
        addrs = socket.getaddrinfo(domain, None)
        for item in addrs:
            if item[4][0] not in ip_list:
                ip_list.append(item[4][0])
    except:
        logger.exception("get_host_iplist error")
        
    return ip_list

def get_host_byname(domain:str):
    #获取域名的第一条IP
    return socket.gethostbyname(domain)

def str_is_ip(str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False


if __name__ == '__main__':
    print( get_out_ip(method=2) )
    print(get_local_ip())
    
