"""可以将电影短评的评论者入库 且保证不重复"""
import pymysql


class Sql:
    def __init__(self):
        """初始化数据库"""
        self.db = pymysql.connect(host="localhost", user="root", password="white", database="DoubanSpider")
