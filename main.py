"""创建线程 用多线程爬取并入库"""
from Spider import *
from Sql import *
import threading

# 初始化数据库
sql = Sql()
global id
global pages_cnt
done = 0


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
        # 输出进度
        global done
        global pages_cnt
        done += 1
        print(f"{done}/{pages_cnt}")


def main():
    """主函数"""

    # 输入影片id
    global id
    id = input("请输入影片id:")
    threadings_cnt = int(input("请输入使用的线程数:"))
    1292001
    # 若该影片没有表格,则为其创建表格
    if not sql.is_table_existed(id):
        sql.create_table(id)
    # 获得该影片页数
    global pages_cnt
    pages_cnt = get_pages_cnt(id)
    # 分配每个线程爬取的页数
    pages_threading = pages_cnt // threadings_cnt
    # 分配线程爬取入库
    print(f"正在以{threadings_cnt}线程爬取{id}......")
    for cnt in range(threadings_cnt):
        bpage = pages_threading * cnt + 1
        epage = pages_threading * (cnt + 1)
        if cnt == threadings_cnt - 1:
            # 最后一个线程要爬完
            epage = pages_cnt
        # 创建线程
        t = threading.Thread(target=get_datas, args=[id, bpage, epage])
        t.start()


if __name__ == "__main__":
    main()
