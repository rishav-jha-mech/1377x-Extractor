import json
import time
import requests
from bs4 import BeautifulSoup

import os
import re

def sanitize_filename(filename):
    """
    Sanitize a filename by replacing all non-alphanumeric characters with underscores.
    """
    return re.sub(r'[^\w\d]+', '_', filename)

i = 28

for x in range(0,151):
    print('Scraping page ...', x)
    response = requests.get(f'https://www.1377x.to/sub/28/{x}')
    html = response.content28
    soup = BeautifulSoup(html, 'html.parser')
    try:
        title_page = soup.title.string
        title_page = sanitize_filename(title_page)
        datas = soup.find_all('table', class_='table')[0]
        rows = soup.find_all('tr')
        results = []

        for i, row in enumerate(rows):
            if i == 0:
                continue
            title = row.find('td', class_='coll-1 name').find_all('a')[1].text.strip()
            link = row.find('td', class_='coll-1 name').find_all('a')[1]['href']
            seeds = int(row.find('td', class_='coll-2 seeds').text.strip())
            leeches = int(row.find('td', class_='coll-3 leeches').text.strip())
            date = row.find('td', class_='coll-date').text.strip()
            size = row.find('td', class_='coll-4 size mob-uploader').text.strip()
            uploader = row.find('td', class_='coll-5 uploader').text.strip()    
            results.append({
                'title': title,
                'link': link,
                'seeds': seeds,
                'leeches': leeches,
                'date': date,
                'size': size,
                'uploader': uploader,
            })

        # Write the results to the JSON file
        with open(f'{title_page}.json', 'a') as f:
            json.dump(results, f)
            f.write('\n')
    time.sleep(2)
    except Exception as e:
        print('Error on page ...', x, e)
        with open(f'error-{i}-{x}.html', 'a') as f:
            f.write(soup.prettify())
        continue
