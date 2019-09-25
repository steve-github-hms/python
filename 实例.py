from selenium import webdriver
import time
import re
import pymysql
def open_sql():
    db = pymysql.connect('localhost', 'root', '1999625', 'python')
    cursor = db.cursor()
    print("连接成功！")
    cursor.execute("DROP TABLE IF EXISTS TAOBAO")
    sql = """CREATE TABLE TAOBAO (
            name CHAR(255) NOT NULL,
            picture CHAR(255),
            price CHAR(25) )"""
    cursor.execute(sql)
    return cursor,db
def search_taobao():
    dr.find_element_by_id('q').send_keys(keyword)
    dr.find_element_by_class_name('btn-search').click()
    time.sleep(15)
    token = dr.find_element_by_xpath(
        '//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    token = int(re.compile(r'\d+').search(token).group(0))
    return token
# https://s.taobao.com/search?q=python&s=44


def drop_down():
    for x in range(1, 11, 2):
        time.sleep(0.5)
        j = x / 10
        js = 'document.documentElement.scrollTop=document.documentElement.scrollHeight * %f' % j
        dr.execute_script(js)


def next_page():
    token = search_taobao()
    num = 0
    while num != 1:#token - 1:
        dr.get('https://s.taobao.com/search?q={}&s={}'.format(keyword, 44 * num))
        dr.implicitly_wait(10)  # 隐式等待（10秒前进入即可）
        num += 1
        drop_down()
        get_product()


def get_product():
    cursor,db=open_sql()
    things=[]
    lis = dr.find_elements_by_xpath(
        '//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for li in lis:
        info = li.find_element_by_xpath(
            './/div[@class="row row-2 title"]').text
        image = li.find_element_by_xpath(
            './/div[@class="pic"]/a/img').get_attribute('src')
        price=li.find_element_by_xpath('.//div[@class="price g_price g_price-highlight"]/strong').text
        things.append([info,image,price])
        print(info + '|' + image+'|'+price)
    for thing in things:
        insert_goods=("INSERT INTO TAOBAO(name,picture,price)" "VALUES(%s,%s,%s)")
        data=(thing[0],thing[1],thing[2])
        cursor.execute(insert_goods,data)
        db.commit();
    db.close()


if __name__ == '__main__':
    keyword = input('输入你要找的商品：')
    dr = webdriver.Chrome()
    dr.get('https://www.taobao.com/')
    next_page()
