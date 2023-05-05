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


for i in range(1,73):
        x=1
        print('Scraping page ...', i)
        response = requests.get(f'https://www.1377x.to/sub/{i}/{x}')
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        try:
            title_page = soup.title.string
            # title_page = sanitize_filename(title_page)
            results = []

            results.append({
                'subno': i,
                'title': title_page,
            })

            # Write the results to the JSON file
            with open(f'subData,json', 'a') as f:
                json.dump(results, f)
                f.write('\n')
            
        except Exception as e:
            print('Error on page ...', x, e)
            with open(f'error-{i}-{x}.html', 'a') as f:
                f.write(soup.prettify())
            continue
