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