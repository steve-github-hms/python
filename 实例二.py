from selenium import webdriver
import requests
import time
import re


def search_picture():
    dr.find_element_by_id('kw').send_keys(keyword)
    dr.find_element_by_class_name('s_search').click()


def drop_down():
    for x in range(1, 11, 2):
        time.sleep(0.5)
        j = x / 10
        js = 'document.documentElement.scrollTop=document.documentElement.scrollHeight * %f' % j
        dr.execute_script(js)


def get_picture():
    num = 0
    picture = []
    lis = dr.find_elements_by_xpath(
        '//ul[@class="imglist clearfix pageNum0"]/li[@class="imgitem"]')
    for i in lis:
        print(num)
        print(num0)
        if num == int(num0):
            break
        drop_down()
        imag = i.find_element_by_xpath(
            './/img[@class="main_img img-hover"]').get_attribute('data-imgurl')
        print(imag)
        picture.append(imag)
        num += 1
    return picture


def install_picture():
    print(len(n))
    t = 0
    for i in n:
        r = requests.get(i)
        path = i[-10:]
        # end=re.search('.jpg$|.jpeg|.gif$|.png',path)
        # if end == None:
        # path=path+'.jpg'
        print(path)
        with open('img/' + str(t) + path, 'wb') as f:
            f.write(r.content)
        t += 1


dr = webdriver.Chrome()
dr.get('http://image.baidu.com/')
keyword = input("输入你要查找的图片：")
num0 = input('输入你要下载的数量：')
search_picture()
n = get_picture()
install_picture()
