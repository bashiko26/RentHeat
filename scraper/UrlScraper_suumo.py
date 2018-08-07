# coding: utf-8

import sys
import os
import urllib.request
from bs4 import BeautifulSoup
import configparser
import psycopg2

class UrlScraper:
    base_url = 'https://suumo.jp/chintai/soba/tokyo/ensen/'

    def scrape_line_url(self):
        html = urllib.request.urlopen(self.base_url)
        soup = BeautifulSoup(html, 'html.parser')
        
        all_line_area = soup.find('table', class_='searchtable')
        line_areas = all_line_area.find_all('tr')
        
        result = []

        for line_area in line_areas:
            line_rows = line_area.find_all('ul', class_='searchitem-list')
            
            for line_row in line_rows:
                lines = line_row.find_all('li')

                for line in lines:
                    line_dict = {}
                    line_name = line.find('a').string
                    line_url  = 'https://suumo.jp' + line.find('a').get('href')
                    line_dict['name'] = line_name
                    line_dict['url']  = line_url
                    result.append(line_dict)
    
        return result

    def createInsert(self, line_list):
        insert_sql = 'Insert into m_line values \n'
        
        for e in line_list:
            values = "('" + e['name'] + "', '" + e['url'] + "'),\n"
            insert_sql += values

        return insert_sql[:-2]

    def get_connection(self):
        name = os.path.dirname(os.path.abspath(__name__))
        joined_path = os.path.join(name, '../env/dbconf.ini')
        path = os.path.normpath(joined_path)

        db_config = configparser.ConfigParser()
        print(path)
        db_config.read(path)

        db = db_config['Postgres']['db']
        host = db_config['Postgres']['host']
        user = db_config['Postgres']['user']
        pw = db_config['Postgres']['password']

        return psycopg2.connect(database=db, host=host, user=user, password=pw)

    def insert(self, sql):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)

if __name__ == '__main__':
    scraper = UrlScraper()
    line_info = scraper.scrape_line_url()
    sql = scraper.createInsert(line_info)
    scraper.insert(sql)
    print(sql)
