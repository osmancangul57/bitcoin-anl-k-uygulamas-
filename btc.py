import requests
from bs4 import BeautifulSoup

url = requests.get("https://coinmarketcap.com/")

cagır = BeautifulSoup(url.content)

btc = cagır.findAll("a",{"href":"/currencies/bitcoin/markets/"})
eth = cagır.findAll("b",{"href":"/currencies/ethereum/markets/"})

for b in btc:
    sayac = b.text
    print(sayac)


