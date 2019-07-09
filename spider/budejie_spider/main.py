import csv
import threading
from queue import Queue

import requests
from lxml import etree


class budejieSpider(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    def __init__(self, page_queue, joke_queue, *args,  **kwargs):
        super(budejieSpider, self).__init__(*args,  **kwargs)
        self.base_domain = "http://www.budejie.com"
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            response = requests.get(url, headers=self.headers)
            text = response.text
            html = etree.HTML(text)
            descs = html.xpath("//div[@class='j-r-list-c-desc']")
            for desc in descs:
                jokes = desc.xpath(".//text()")
                joke = "\n".join(jokes).strip()
                link = self.base_domain+desc.xpath(".//a/@href")[0]
                self.joke_queue.put((joke, link))
            print('第%s页下载完成！' % url.split('/')[-1])

class budejieWriter(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    def __init__(self, joke_queue, writer, gLock, *args,  **kwargs):
        super(budejieWriter, self).__init__(*args,  **kwargs)
        self.joke_queue = joke_queue
        self.writer = writer
        self.lock = gLock

    def run(self):
        while True:
            try:
                joke_info = self.joke_queue.get(timeout=40)
                joke, link = joke_info
                self.lock.acquire()
                self.writer.writerow((joke, link))
                self.lock.release()
                print('保存一条.')
            except:
                pass

def main():
    page_queue = Queue(10)
    joke_queue = Queue(500)
    gLock = threading.Lock()
    fp = open('budejie.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('content', 'link'))

    for x in range(1, 11):
        url = 'http://www.budejie.com/text/%d' % x
        page_queue.put(url)

    for x in range(5):
        t = budejieSpider(page_queue, joke_queue)
        t.start()

    for x  in range(5):
        t = budejieWriter(joke_queue, writer, gLock)
        t.start()

if __name__ == "__main__":
    main()
