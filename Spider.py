import requests
import bs4
import re


def get_pages_cnt(id):
    """获得单个影片的长评页码"""
    # 准备请求
    url = f"https://movie.douban.com/subject/{id}/reviews"
    headers = {
        "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      r"Chrome/88.0.4324.150 Safari/537.36"}
    # 发送请求
    res = requests.get(url=url, headers=headers)
    # bs4解析请求
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    commonts_cnt_data = soup.find("div", class_="movie-content review-wrapper").div.h1.text

    # 获得页码
    commonts_cnt = int(re.findall("影评 \((.*?)\)", commonts_cnt_data)[0])
    page_cnt = commonts_cnt // 20
    if commonts_cnt % 20 != 0:
        page_cnt += 1
    return page_cnt


def get_commonters(id, page):
    """获得单个电影特定页数的评论者"""
    # 准备请求
    start = 20 * (page - 1)
    url = f"https://movie.douban.com/subject/{id}/reviews?start={start}"
    print(url)
    headers = {
        "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      r"Chrome/88.0.4324.150 Safari/537.36"}
    # 发送请求
    res = requests.get(url=url, headers=headers)
    # bs4解析得到评论者用户名
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    commonts = soup.find_all("a", class_="name")
    commonters = []
    for commont in commonts:
        commonters.append(commont.text)
    # 返回
    return commonters


def main():
    """主函数"""
    print(get_commonters(1292052, 539))
    print(get_pages_cnt(1292052))


if __name__ == "__main__":
    main()
