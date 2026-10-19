from bs4 import BeautifulSoup
from fetch import get, write_csv
from urllib.parse import urljoin
import re

BASE_URL = 'https://www.pcworth.com'
soup = BeautifulSoup(get('https://www.pcworth.com/c/gpu'), 'lxml')
products = soup.find_all('div', {'data-testid':'product-card'})

def clean_price(text):
    return float(re.sub(r"[^\d.]", "", text))
    
def stockStatus(text):
    if text == 'In stock':
        return True
    else:
        return False

rows = []

for product in products:
    rows.append({
        'title': product.select_one('h3').get_text(),
        'price': clean_price(product.find('span', {'class':'MuiBox-root mui-1k4bksz'}).get_text()),
        'srp': clean_price(product.find('span', {'class':'MuiBox-root mui-15q9t9w'}).get_text()),
        'brand': product.find('span', {'class': 'MuiTypography-root MuiTypography-body1 mui-8677jg'}).get_text(),
        'in_stock': stockStatus(product.find('p').get_text()),
        'url': urljoin(BASE_URL, product.find('a').attrs['href'])
    })

write_csv(rows, 'pcworth.csv')
print(clean_price("₱17,354.4 (SRP)"))
