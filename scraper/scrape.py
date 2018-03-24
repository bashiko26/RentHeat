# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup

class Scrape:
 
    def get_price(self, url):
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        
        # get title
        title = soup.title.string
        print("title: " + title)
        
        # get update date
        update_date = soup.find("p", class_="graph-updated").string
        print("update date: " + update_date)
        
        # get rent list
        rent_list = soup.find_all("tr", class_="js-graph-data")
        for rent in rent_list:
            floor = rent.find("td").string
            price_i = float(rent.find("span").string)*10
            price = str(price_i)
            
            print(floor + "\t: " + price + " K yen")


if __name__ == '__main__':
    url_nishifuna = 'https://suumo.jp/chintai/soba/chiba/ek_29360/'
    scrape = Scrape()
    scrape.get_price(url_nishifuna)

