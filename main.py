"""创建线程 用多线程爬取并入库"""
from Spider import *
from Sql import *

# 初始化数据库
sql = Sql()
global id


def get_datas(id, bpage, epage):
    """用于爬取该电影在bpage~epage范围内的数据"""
    for page in range(bpage - 1, epage + 1):
        # 处理每一页的评论者
        commonters = get_commonters(id, page)
        for commonter in commonters:
            # 跳过已注销账号
            if id == "[已注销]":
                continue
            if not sql.is_commontor_existed(id, commonter):
                # 该评论者之前未被记录,则记录
                sql.insert_commentor(id, commonter)


def main():
    """主函数"""

    # 输入影片id
    global id
    id = input("请输入影片id:")
    # 若该影片没有表格,则为其创建表格
    if not sql.is_table_existed(id):
        sql.create_table(id)
    get_datas(id, 3, 4)

    # 获得该影片页数

    # 分配线程爬取入库


if __name__ == "__main__":
    main()
