import json
import requests
import psutil


def get_ip(flag):
    if flag == 0:
        return '请选择上网方式'
    info = psutil.net_if_addrs()
    card_info = []
    for k, v in info.items():
        for item in v:
            if item[0] == 2:
                card_info.append((k, item[1]))
    for i, m in card_info:
        for ip in m:
            if flag == 1:
                if i == '以太网':
                    return m
            elif flag == 2:
                if i == 'WLAN':
                    return m


def check(usr_ip):
    chk = requests.session()

    check_url = 'http://10.10.244.11:801/eportal/'

    check_payload = {
        'c': 'ACSetting',
        'a': 'checkScanIP',
        'callback': 'jQuery11130026949342982102165_1648792503262',
        'wlanuserip': usr_ip,
        '_': '1648792503263'
    }

    check_headers = {
        'Host': '10.10.244.11:801',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.60 Safari/537.36',
        'DNT': '1',
        'Accept': '*/*',
        'Referer': 'http://10.10.244.11/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    chk_content = chk.get(url=check_url, params=check_payload, headers=check_headers)
    chk_content.encoding = 'utf8'

    json_content = json.loads(chk_content.text[45:len(chk_content.text) - 1])
    return json_content


def connect(usr_ip, usr_name, usr_pwd, operator):
    conn = requests.session()

    connect_url = 'http://10.10.244.11:801/eportal/'

    connect_payload = {
        'c': 'ACSetting',
        'a': 'Login',
        'protocol': 'http:',
        'hostname': '10.10.244.11',
        'iTermType': '1',
        'wlanuserip': usr_ip,
        'wlanacip': 'null',
        'wlanacname': 'XL-BRAS-SR8806-X',
        'mac': '00-00-00-00-00-00',
        'ip': usr_ip,
        'enAdvert': '0',
        'queryACIP': '0',
        'loginMethod': '1'
    }

    if operator == 'njupt':
        operator = ''
    elif operator == 'cmcc':
        operator = '@cmcc'
    elif operator == 'chinanet':
        operator = '@chinanet'

    connect_data = {
        "DDDDD": ",0," + usr_name + operator,
        "upass": usr_pwd,
        "0MKKey": "123456"
    }

    conn.post(url=connect_url, params=connect_payload, data=connect_data)

    return check(usr_ip)


def disconnect(usr_ip):
    discon = requests.session()

    disconnect_url = 'http://10.10.244.11:801/eportal/'

    disconnect_payload = {
        'wlanuserip': usr_ip,
        'wlanacname': 'XL-BRAS-SR8806-X',
        'wlanacip': 'null',
        'session': '',
        'queryACIP': '0',
        'port': '',
        'mac': '',
        'iTermType': '1',
        'hostname': '10.10.244.11',
        'c': 'ACSetting',
        'a': 'Logout'
    }

    disconnect_headers = {
        'Host': '10.10.244.11:801',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.60 Safari/537.36',
        'Referer': 'http://10.10.244.11/'
    }

    tem = discon.post(url=disconnect_url, params=disconnect_payload, headers=disconnect_headers, allow_redirects=False)
    print(tem.url)
    return check(usr_ip)
