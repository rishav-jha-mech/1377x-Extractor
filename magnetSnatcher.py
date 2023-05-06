import json
import time
import requests
from bs4 import BeautifulSoup
from utils import sanitize_filename



def magnetSnatcher(relative_url, x):
    response = requests.get(f'https://www.1377x.to/torrent/{relative_url}')
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')

    try:
        title = soup.title.string
        genres = [span.text.strip() for span in soup.find('div', class_='torrent-category').find_all('span')]
        description = soup.find('p').text.strip()
        magnet_links = []
        images = []

        for link in soup.find_all('a', href=True):
            href_value = link['href']
            if href_value.startswith('magnet:'):
                magnet_links.append(href_value)

        for img in soup.find_all('img',class_='img-responsive descrimg'):
            img_value = img['src']
            if img_value.startswith('https://'):
                images.append(img_value)

        results = {
            'title': title,
            'img': images,
            'genres': genres,
            'description': description,
            'magnet_links': magnet_links,
        }
        
        with open(f'{sanitize_filename(title)}.json', 'a') as f:
            f.write('[\n')
            json.dump(results, f)
            f.write('\n]')

    except Exception as e:
        print('Error on page ...', x, e)
        with open(f'error-{i}-{x}.html', 'a') as f:
            f.write(soup.prettify())