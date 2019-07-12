# Scrapy

## 安装Scrapy框架
- 安装scrapy: 通过`pip install scrapy`安装
- 在ubuntu上安装scrapy之前，需要先安装以下依赖：`sudo apt-get install python3-dev build-essential python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev`，然后再通过`pip install scrapy`安装。
- 如果在windows系统下，提示这个错误ModuleNotFoundError: No module named 'win32api'，那么使用以下命令可以解决：`pip install pypiwin32`。

## 创建项目和爬虫
- 创建项目：`scrapy startproject [项目名称]`
- 创建爬虫：进入项目所在路劲，执行命令：`scrapy genspider [爬虫名称] [爬虫的域名]` 。注意，爬虫的名称不能和项目名称一致

## 框架模块功能
- Scrapy Engine（引擎）：Scrapy框架的核心部分。负责在Spider和ItemPipeline、Downloader、Scheduler中间通信、传递数据等。
- Spider（爬虫）：发送需要爬取的链接给引擎，最后引擎把其他模块请求回来的数据再发送给爬虫，爬虫就去解析想要的数据。这个部分是我们开发者自己写的，因为要爬取哪些链接，页面中的哪些数据是我们需要的，都是由程序员自己决定。
- Scheduler（调度器）：负责接收引擎发送过来的请求，并按照一定的方式进行排列和整理，负责调度请求的顺序等。
- Downloader（下载器）：负责接收引擎传过来的下载请求，然后去网络上下载对应的数据再交还给引擎。
- Item Pipeline（管道）：负责将Spider（爬虫）传递过来的数据进行保存。具体保存在哪里，应该看开发者自己的需求。
- Downloader Middlewares（下载中间件）：可以扩展下载器和引擎之间通信功能的中间件。
- Spider Middlewares（Spider中间件）：可以扩展引擎和爬虫之间通信功能的中间件。

## 目录结构介绍
- items.py：用来存放爬虫爬取下来数据的模型。
- middlewares.py：用来存放各种中间件的文件。
- pipelines.py：用来将items的模型存储到本地磁盘中。
- settings.py：本爬虫的一些配置信息（比如请求头、多久发送一次请求、ip代理池等）。
- scrapy.cfg：项目的配置文件。
- spiders包：以后所有的爬虫，都是存放到这个里面。

## Scrapy爬虫注意事项
- response 是一个`from scrapy.http.response.html.HtmlResponse`对象，可以执行`xpath`和`css`语法提取数据
- 提取出来的数据是一个`Selector`或者`SelectorList`对象，如果想要获取其中的字符串，应该执行`getall`或者`get`方法
- getall方法：获取`Selector`中所有文本，返回的是一个列表
- get方法：获取的是`Selector`中的第一个文本，返回的是str类型
- 如果数据解析回来要传给pipelines处理，可以使用`yield`来返回，或者是添加所有的item，统一使用`return`返回
- item：在`item.py`中定义好模型，不要使用字典
- pipelines：这个是专门一从来保存数据的，其中有三个方法是会被经常用到的。要激活pipelines，应该在`settings.py`中，设置`ITEM_PIPELINES`
    - `open_spider`：当爬虫被打开的时候执行
    - `process_item`：当爬虫有item传过来的时候会被调用
    - `close_spider`：当爬虫关闭的时候被调用


## JsonItemExporter和JsonLinesItemExporter
- 保存json数据的时候，可以使用这两个类，让操作变得更简单
- `JsonItemExporter`：每次把数据添加到内存中，最后统一写入磁盘，存储的数据是一个满足json规则的数据，数据量比较大，比较耗内存
    ```python
    from scrapy.exporters import JsonItemExporter
    class QsbkPipeline(object):
        def __init__(self):
            self.fp = open("duanzi.josn", 'wb')
            self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
            self.exporter.start_exporting()

        def open_spider(self, spider):
            print('start...')

        def process_item(self, item, spider):
            self.exporter.export_item(item)
            return item

        def close_spider(self, spider):
            self.exporter.finish_exporting()
            self.fp.close()
            print('end...')
    ```
- `JsonLinesItemExporter`：每次调用`export_item`的时候把这个item存储到磁盘，每一个字典是一行，整个文件不是一个满足json格式的文件，每次处理初级的时候直接存储到硬盘，不耗内存，数据比较安全
    ```python
    from scrapy.exporters import JsonLinesItemExporter
    class QsbkPipeline(object):
        def __init__(self):
            self.fp = open("duanzi.josn", 'wb')
            self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

        def open_spider(self, spider):
            print('start...')

        def process_item(self, item, spider):
            self.exporter.export_item(item)
            return item

        def close_spider(self, spider):
            self.fp.close()
            print('end...')
    ```

## CrawlSpider
- 需要使用`LinkExtractor`和`Rule`
- allow设置规则的方法：要能够限制在我们想要的url上面，不要跟其他url产生相同的正则表达式即可
- 什么情况下使用follow：如果在爬取页面的时候，需要将满足当前条件的url再进行跟进，否则设置为False
- 什么情况下该指定callback：如果这个url对应的页面，只是为了获取更多的url，并不需要里面的数据，那么可以不指定callback，如果想要获取url对应页面的数据，那么就需要指定一个callback

## 运行爬虫
`scrapy crawl qsbk_spider`