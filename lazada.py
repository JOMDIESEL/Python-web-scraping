#lazada.py

from selenium import webdriver
import time
from bs4 import BeautifulSoup as soup

opt = webdriver.ChromeOptions()
opt.add_argument('headless')


def checkprice(url):
	driver = webdriver.Chrome(options=opt)
	driver.get(url)
	time.sleep(3)

	page_html = driver.page_source
	#print(driver.page_source)

	data = soup(page_html,'html.parser')
	product = data.findAll('div',{'class':'c16H9d'})
	price = data.findAll('span',{'class':'c13VH6'})

	all_product = []
	all_url = []
	all_price = []

	for pd in product:
		print(pd.text)
		print('https:'+ pd.a['href'])

		all_product.append(pd.text)
		all_url.append('https:'+ pd.a['href'])


	for pc in price:
		#print(pc.text)
		pc_text = pc.text
		pc_text = pc_text.replace('฿','')
		pc_text = pc_text.replace(',','')
		all_price.append(float(pc_text))

	return (all_product,all_url,all_price)


url = 'https://www.lazada.co.th/shop-laptops/?spm=a2o4m.home.cate_1.3.1125515fmDrUwT'
checkprice(url)


