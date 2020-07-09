import requests


def send_req():
    """GET https://www.weizan.cn/f/s-1102881?page=3&typeId=528804 HTTP/1.1
Host: www.weizan.cn
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9"""

    """发送请求"""

    url = "https://www.weizan.cn/f/s-1102881?page=3&typeId=528804"
    headers = {
        "Host": "www.weizan.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",

    }
    response = requests.get(url=url, headers=headers, verify=False).content
    print(response)

    with open('zufang.html', 'wb') as f:
        f.write(response)

def analysis():
    with open('zufang.html', 'wb') as f:
if __name__ == '__main__':
    send_req()
