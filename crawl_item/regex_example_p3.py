import re
import urllib.request

def scrape(html):
	area = re.findall('<tr id="places_area__row">.*?<td class="w2p_fw">(.*?)</td>',html)[0]
	#area = re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)[0]
	print('area=',area)
	return area

html=urllib.request.urlopen('http://example.webscraping.com/places/default/view/Aland-Islands-2').read().decode('utf-8')
print('html=',html)
print('area=',scrape(html))