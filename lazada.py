from selenium import webdriver
import time
from bs4 import BeautifulSoup as soup

options = webdriver.ChromeOptions()
options.add_argument('headless')

def check_price(url):
    # เปิดเบราว์เซอร์ด้วย WebDriver
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)

    # ดึง HTML จากหน้าเว็บ
    page_html = driver.page_source
    data = soup(page_html, 'html.parser')
    
    # ค้นหาข้อมูลสินค้าและราคา
    products = data.findAll('div', {'class': 'c16H9d'})
    prices = data.findAll('span', {'class': 'c13VH6'})

    all_products = []
    all_urls = []
    all_prices = []

    # วนลูปเพื่อดึงข้อมูลสินค้าและ URL
    for product in products:
        print(product.text)
        print('https:' + product.a['href'])

        all_products.append(product.text)
        all_urls.append('https:' + product.a['href'])

    # วนลูปเพื่อดึงข้อมูลราคา
    for price in prices:
        price_text = price.text
        price_text = price_text.replace('฿', '')
        price_text = price_text.replace(',', '')
        all_prices.append(float(price_text))

    return all_products, all_urls, all_prices

# URL ของหน้า Lazada ที่ต้องการตรวจสอบราคา
url = 'https://www.lazada.co.th/shop-laptops/?spm=a2o4m.home.cate_1.3.1125515fmDrUwT'
check_price(url)
