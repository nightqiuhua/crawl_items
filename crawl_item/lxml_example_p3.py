import re
import urllib.request
import lxml.html

def scrape(html):
	tree = lxml.html.fromstring(html)
	td = tree.cssselect('tr.f>td>div.right>div.pagenav>a')[3]
	print("td=",tree.cssselect('tr.f>td>div.right>div.pagenav>a'))
	area= td.get('href')#.get('属性名') 获取属性值  .text_content() 获取元素文本
	return area

html = urllib.request.urlopen('https://hr.tencent.com/position.php?&start=0').read().decode('utf-8')
print('area=',scrape(html))