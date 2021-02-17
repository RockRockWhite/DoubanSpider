"""可以将电影短评的评论者入库 且保证不重复"""
import pymysql


class Sql:
    def __init__(self):
        """初始化数据库"""
        self.db = pymysql.connect(host="localhost", user="root", password="white", database="DoubanSpider")

    def is_table_existed(self, id):
        """判断该电影的table是否存在"""
        cursor = self.db.cursor()
        commond = f"show tables like '{id}'"
        cursor.execute(commond)
        data = cursor.fetchone()
        if data == None:
            return True
        else:
            return False

    def create_table(self, id):
        """用于为电影创建新的table"""
        cursor = self.db.cursor()
        commond = f"create table {id} (name varchar(255))"
        cursor.execute(commond)
        self.db.commit()


def main():
    sql = Sql()
    print(sql.is_table_existed("test4"))


if __name__ == '__main__':
    main()
