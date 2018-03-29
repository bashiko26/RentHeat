# coding: utf-8

import sys
import urllib.request
from bs4 import BeautifulSoup

class Scrape:
 
    def get_price(self, url):
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        
        # get title
        title = soup.title.string
        print('title: ' + title)
        
        # get update date
        update_date = soup.find('p', class_='graph-updated').string
        print('$B99?7F|(B: ' + update_date)
        
        # get rent list
        rent_list = soup.find_all('tr', class_='js-graph-data')
        for rent in rent_list:
            floor = rent.find('td').string
            price = rent.find('span').string
            unit = '$BK|1_(B'
            print(floor + '\t: ' + price + unit)

    def get_stations(url):
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        # get title

        # get line

        # return station list

if __name__ == '__main__':
    url_nishifuna = 'https://suumo.jp/chintai/soba/chiba/ek_29360/'
    scrape = Scrape()
    scrape.get_price(url_nishifuna)

