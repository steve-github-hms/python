import requests
import parsel
import pprint
import threading
re = requests.get('https://movie.douban.com/top250')
# print(re.text)
sel = parsel.Selector(re.text)
#threading.Thread
pprint.pprint(sel.re('<span class="title">(.*?)</span>'))
pprint.pprint(sel.xpath('//*[@class="inq"]/text()').getall())
