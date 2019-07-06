import requests
import re

def parse_page(url):
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Referer': 'www.gushiwen.org'
    }

    response = requests.get(url, headers=HEADERS)
    text = response.text
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    dynasties= re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors= re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    contents_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>', text, re.DOTALL)

    contents = []
    for content in contents_tags:
        x =  re.sub(r'<.*?>', '', content)
        contents.append(x.strip())

    # print(titles)
    # print(dynasties)
    # print(authors)
    # print(contents)

    poems = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content
        }
        poems.append(poem)
    
    for poem in poems:
        print(poem)
        print('~'*100)

def main():
    url = 'https://www.gushiwen.org'
    parse_page(url)

if __name__ == "__main__":
    main()