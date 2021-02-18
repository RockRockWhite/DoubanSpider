"""可以将电影短评的评论者入库 且保证不重复"""
import pymysql


class Sql:
    def __init__(self):
        """初始化数据库"""
        self.db = pymysql.connect(host="localhost", user="root", password="white", database="DoubanSpider")

    def is_table_existed(self, id):
        """判断该电影的table是否存在"""
        cursor = self.db.cursor()
        commond = f"show tables like 't{id}'"
        cursor.execute(commond)
        data = cursor.fetchone()
        if data is None:
            return False
        else:
            return True

    def create_table(self, id):
        """用于为电影创建新的table"""
        cursor = self.db.cursor()
        commond = f"create table t{id} (name varchar(255))"
        cursor.execute(commond)
        self.db.commit()

    def is_commontor_existed(self, id, name):
        """判断该电影中该评论者是否已经被记录"""
        cursor = self.db.cursor()
        commond = f'select * from t{id} where name="{name}"'
        cursor.execute(commond)
        data = cursor.fetchone()
        if data is None:
            return False
        else:
            return True

    def insert_commentor(self, id, name):
        """向该电影的数据库插入该评论者"""
        cursor = self.db.cursor()
        commond = f'insert into t{id} values ("{name}")'
        cursor.execute(commond)
        self.db.commit()


def main():
    sql = Sql()
    print(sql.is_table_existed("test4"))
    print(sql.is_commontor_existed("test4", "wdnmd3"))
    sql.insert_commentor("test4", "wdnmd3")


if __name__ == '__main__':
    main()
