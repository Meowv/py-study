# -*- coding: utf-8 -*-

import pymysql
from pymysql import cursors
from twisted.enterprise import adbapi


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
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql, (item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['origin_url'],item['article_id']))
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

class JianshuTwistedSpiderPipeline(object):
    def __init__(self):
        dbparams = {
            'host' : 'rm-uf664xe30hl1i9c09qo.mysql.rds.aliyuncs.com',
            'user' : 'root',
            'password' : 'ABCdef123456',
            'database' : 'jianshu',
            'port' : 3306,
            'charset' : 'utf8',
            'cursorclass': cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        self._sql = None

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
                insert into article(title,content,author,avatar,pub_time,origin_url,article_id,origin_url,read_count,like_count,word_count,subjects,omments_count) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            return self._sql
        return self._sql

    def process_item(self, item, spider):
        defer =  self.dbpool.runInteraction(self.insert_item, item)
        defer.addErrback(self.handler_error, item, spider)

    def insert_item(self, cursor, item):
        cursor.execute(self.sql, (item['title'],item['content'],item['author'],item['avatar'],item['pub_time'],item['origin_url'],item['article_id']))

    def handler_error(self, error, item, spider):
        print('~'*10 + 'error'+ '~'*10)
        print(error)
        print('~'*10 + 'error'+ '~'*10)
