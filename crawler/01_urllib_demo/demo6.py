from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

def get_opener():
    # 1.登录
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    # 1.4 使用opener发送登录的请求
    return opener

def login_renren(opener):
    data = {
        'email': '...',
        'password': '...'
    }
    login_url = "http://www.renren.com/PLogin.do"
    req = request.Request(login_url,data=parse.urlencode(data).encode('utf-8'),headers=headers)
    opener.open(req)

def visit_profile(opener):
    # 2. 访问
    dapeng_url = "http://www.renren.com/880151247/profile"
    # opener已经包含登录所需cookie数据
    req = request.Request(dapeng_url,headers=headers)
    resp = opener.open(req)

    html = resp.read().decode('utf-8')
    with open('renren.html', 'w', encoding='utf-8') as fp:
        fp.write(html)

if __name__ == "__main__":
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)