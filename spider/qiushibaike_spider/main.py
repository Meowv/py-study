import requests
import re

def parse_page(url):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(url, headers=HEADERS)
    text = response.text
    contents = re.findall(r'<div class="content">.*?<span>(.*?)</span>.*?</div>', text, re.DOTALL)

    duanzi = []
    for content in contents:
        x = re.sub(r'<.*?>', '', content)
        duanzi.append(x.strip())
        print(x.strip())
        print('~'*100)

def main():
    for x in range(1, 10):
        url = 'https://www.qiushibaike.com/text/page/%s/' % x
        parse_page(url)

if __name__ == "__main__":
    main()