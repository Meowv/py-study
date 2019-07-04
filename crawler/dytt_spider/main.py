from lxml import etree
import requests

BASE_DOMAIN = 'https://www.dytt8.net'

HEADERES = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

def get_detail_urls(url):
    response = requests.get(url, headers=HEADERES)

    text = response.content.decode('gbk')
    html = etree.HTML(text)

    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url: BASE_DOMAIN + url, detail_urls)

    return detail_urls

def parse_detail_page(url):
    pass

def spider():
    base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    for x in range(1, 198):
        url = base_url.format(x)
        movie = parse_detail_page(url)

if __name__ == "__main__":
    spider()