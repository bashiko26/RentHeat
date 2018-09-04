# coding: utf-8

import sys
import urllib.request
from bs4 import BeautifulSoup

class RentScraper:
 
    def get_price(self, url):
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, 'html.parser')
        
        # get title
        title = soup.title.string
        print('タイトル: ' + title)
        
        # get update date
        update_date = soup.find('p', class_='graph-updated').string
        index_month = update_date.find("月")
        index_day = update_date.find("日")
        year = update_date[:4]
        month = update_date[5:index_month]
        day = update_date[index_month+1:index_day]
        date = year + "-" + month + "-" + day
        print('更新日: ' + date)
        
        # get rent list
        rent_list = soup.find_all('tr', class_='js-graph-data')
        result_list = []
        for rent in rent_list:
            floor = rent.find('td').string
            if floor == 'ワンルーム':
                floor = '1R'
            price = rent.find('span').string
            unit = '万円'
            result = {'floor':floor, 'price': price}
            result_list.append(result)
            # print(floor + '\t: ' + price + unit)
        return result_list

    def get_stations(self, url):
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html, "html.parser")

        # get title
        title = soup.title.string
        # print(title)

        # get line
        stations = soup.find_all('tr', class_='js-graph-data')
        station_list = []
        for s in stations:
            name = s.td.a.string
            url = 'https://suumo.jp' + s.a.get('href')
            station_dict = {'name':name, 'url':url}
            station_list.append(station_dict)
            # print(name + '\t:\t' + url)

        # return station list
        return station_list

if __name__ == '__main__':
    url_nishifuna = 'https://suumo.jp/chintai/soba/chiba/ek_29360/'
    scrape = RentScraper()
    # scrape.get_price(url_nishifuna)
    url_sobu = 'https://suumo.jp/chintai/soba/chiba/en_sobusen/'
    stations = scrape.get_stations(url_sobu)
    
    for s in stations:
        print(s['name'])
        # print(s)
        rent_list = []
        rent_list = scrape.get_price(s['url'])

        for rent in rent_list:
            print(
                'name: ' + s['name']
                + '\t, floor: ' + rent['floor']
                + '\t, price: ' + rent['price']
                )
