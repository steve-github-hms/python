import requests
import re
goods = '时间简史'
url = 'http://search.dangdang.com/?key=' + goods + '&act=input'
res = requests.get(url)
res.encoding = res.apparent_encoding
html = res.text
ul = re.findall(r'<ul class="bigimg" id="component_59">.*?<ul>', html, re.S)[0]
ul = ul.replace(
    '</i></a></p><div class=\"lable_label\"><span class=\"new_lable\" y="">',
    '')
info_list = re.findall(r'<a title="(.*?)"\s\sddclick', ul)
price_list = re.findall(r'&yen;(.*?)</span>', ul)
ilt = []
for i in range(len(info_list)):
    tittle = info_list[i]
    price = price_list[i]
    ilt.append([price, tittle])
# print(ul)
# print(info_list)
# print(price_list)
# print(ilt)
tplt = "{:4}\t{:8}\t{:16}"
print(tplt.format("序号", "价格", "商品名称"))
count = 0
for g in ilt:
    count = count + 1
    print(tplt.format(count, g[0], g[1]))
