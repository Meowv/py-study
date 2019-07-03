from urllib import request

dapeng_url = "http://www.renren.com/880151247/profile"

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Cookie': 'anonymid=jxn97nbxwklkux; depovince=GW; _r01_=1; JSESSIONID=abcwKVW-2ro1cdDxk83Uw; ick_login=99af3e58-dfc6-4902-bb22-afc9eba849c7; ick=20d33280-e824-4a3e-943f-110f3bba0029; t=4163b63404421a7eb0584b3cce58cc815; societyguester=4163b63404421a7eb0584b3cce58cc815; id=971368245; xnsid=480e833a; ver=7.0; loginfrom=null; jebe_key=9e8de55b-a345-4861-83c4-98a3538ef073%7C8ddf4c90ebf64a7cc8163133aa871bf1%7C1562159197390%7C1%7C1562159197344; jebe_key=9e8de55b-a345-4861-83c4-98a3538ef073%7C8ddf4c90ebf64a7cc8163133aa871bf1%7C1562159197390%7C1%7C1562159197345; wp_fold=0; jebecookies=af78c114-61fa-4ee7-a743-7eb905301623|||||; Hm_lvt_cdce8cda34e84469b1c8015204129522=1562159131,1562159194,1562159292,1562159346; Hm_lpvt_cdce8cda34e84469b1c8015204129522=1562159482'
}

req =  request.Request(url=dapeng_url,headers=headers)
resp = request.urlopen(req)

html = resp.read().decode('utf-8')

with open('renren.html', 'w', encoding='utf-8') as fp:
    # write 函数必须写入一个 str 的数据类型
    # bytes -> decode -> str
    # str -> encode -> bytes
    fp.write(html)