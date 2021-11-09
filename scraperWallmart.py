import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = 'https://www.walmart.com.ar/buscar?text=leche'

s = Service('./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=s, options=options)
#driver.minimize_window()

driver.get(url)
driver.implicitly_wait(30)
print(f'Driver title: {driver.title}')

#Wallmart:
listaDeProductos = driver.find_elements_by_xpath('//ul//li/div[@class="prateleira__item price-checked"]')
print('\n')
print('=' * 70)
print(f'La cantidad de productos leidos es: {len(listaDeProductos)}')
print('=' * 70)

print('\n')
print('*' * 70)
for producto in listaDeProductos:
    descripcion = producto.find_element_by_xpath('.//div[@class="prateleira__content"]//a[@class="prateleira__name"]').text
    precio = producto.find_element_by_xpath('.//div[@class="prateleira__content"]//a[@class="prateleira__price"]/span[@class="prateleira__best-price originalBestPrice"]').text
    print(F'Descripcion: {descripcion}, {precio}')
    print('-' * 70)
print('*' * 70)

driver.quit()
