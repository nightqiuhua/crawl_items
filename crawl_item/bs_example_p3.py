import urllib.request
from bs4 import BeautifulSoup

def scrape(html):
	soup = BeautifulSoup(html)
	#print('soup=',soup)
	tr = soup.find(attrs={'class':'f'})
	a = tr.find(attrs={'id':'prev'})
	print('a=',a)
	#area = a.text#获取文本
	area = a.get('href')#获取属性值
	print('area =',area)
	return area

html = urllib.request.urlopen('https://hr.tencent.com/position.php?&start=0').read().decode('utf-8')

scrape(html)
