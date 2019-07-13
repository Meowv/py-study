# -*- coding: utf-8 -*-

import pymysql


class JianshuSpiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host' : 'rm-uf664xe30hl1i9c09qo.mysql.rds.aliyuncs.com',
            'user' : 'root',
            'password' : 'ABCdef123456',
            'database' : 'jianshu',
            'port' : 3306,
            'charset' : 'utf8'
        }
        self.conn = pymysql.connect(**dbparams)
        self.coursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.coursor.execute(self.sql, (item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['origin_url'],item['article_id']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into article(title,content,author,avatar,pub_time,origin_url,article_id) values(%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql
