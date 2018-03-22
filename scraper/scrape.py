# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup

def get_price(url):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.string

    print(title)
        
if __name__ == '__main__':
    url = 'https://suumo.jp/chintai/soba/chiba/ek_29360/'
    get_price(url)
