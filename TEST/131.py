# https://m.mm131.net/xinggan/2957.html
"""
GET https://m.mm131.net/xinggan/2957_2.html HTTP/1.1
Host: m.mm131.net
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://m.mm131.net/xinggan/2957.html
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: Hm_lvt_672e68bf7e214b45f4790840981cdf99=1590276545; UM_distinctid=17243de590d832-0161468bc85abe-d373666-1fa400-17243de590edbd; CNZZDATA1277874215=940014182-1590271553-%7C1590271553; Hm_lpvt_672e68bf7e214b45f4790840981cdf99=1590276679




"""
import requests


def send_req():
    # 发送请求
    url = "https://m.mm131.net/xinggan/2957_2.html"
    headers = {
        "Host": "m.mm131.net",
        "Referer": "https://m.mm131.net/xinggan/2957.html",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36",
    }
    response = requests.get(url, headers=headers, verify=False)
    with open('1.html', 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    send_req()
