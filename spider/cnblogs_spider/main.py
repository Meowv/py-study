import requests
from lxml import etree

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    html = etree.HTML(response.text)

    detail_urls = html.xpath("//h3/a[@class='titlelnk']/@href")

    return detail_urls

def parse_detail_page(url):
    response = requests.get(url, headers=HEADERS)
    html = etree.HTML(response.text)

    blogs = {}

    original_url = url
    blogs['original_url'] = original_url

    title = html.xpath("//a[@id='cb_post_title_url']/text()")[0]
    blogs['title'] = title

    post_date = html.xpath("//span[@id='post-date']/text()")[0]
    blogs['post_date'] = post_date

    post_body = html.xpath("//div[@id='cnblogs_post_body']")[0]
    blogs['post_body'] = etree.tostring(post_body, encoding='utf-8').decode('utf-8')
    
    return blogs

def spider():
    base_url = 'https://www.cnblogs.com/cate/dotnetcore/'
    for x in range(1, 10):
        url = base_url + str(x)
        detail_urls = get_detail_urls(url)
        for detial_url in detail_urls:
            blogs = parse_detail_page(detial_url)
            print(blogs)
        break

if __name__ == "__main__":
    spider()