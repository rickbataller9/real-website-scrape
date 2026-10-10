from bs4 import BeautifulSoup
from fetch import get

soup = BeautifulSoup(get("https://www.pcworth.com/c/gpu"), "lxml")
cards = soup.select('[data-testid="product-card"]')
print(len(cards))
print(cards[0].select_one('a[href^="/product/"]')["aria-label"])
