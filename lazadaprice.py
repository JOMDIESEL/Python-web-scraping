#loginweb.py
#pip install selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup as soup

#ทำให้โปรแกรม ไม่ต้องไปเปิดdriver
opt = webdriver.ChromeOptions()
opt.add_argument('headless')
url = 'https://www.lazada.co.th/shop-laptops/?spm=a2o4m.home.cate_1.3.1125719cvwlhRR'

def checkprice(url):
	driver = webdriver.Chrome(options=opt)
	driver.get(url)
	time.sleep(3)
	page_html = driver.page_source

	data = soup(page_html,'html.parser')

	product = data.findAll('div',{'class':'c16h9d'})

	all_product = []
	all_url = []
	all_price = []

	for pd in product:	
		print(pd.text)
		print('https:'+pd.a['href'])

checkprice(url)

#print(driver.page_source)