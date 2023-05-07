import json
import time
import requests
from bs4 import BeautifulSoup
from utils import sanitize_filename, postProcessToJson
from vars import OUTPUT_FOLDER, DATABASE_FOLDER,ERRORS_FOLDER

def magnetSnatcher(data,file_name):
    link = f'https://www.1377x.to{data.get("link")}'
    response = requests.get(link)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    
    try:
        genres = []
        magnet_links = []
        images = []

        title = data.get("title")
        description = soup.find('p').text.strip()
        torrent_category = soup.find('div', class_='torrent-category')

        if torrent_category is not None:
            genres = [span.text.strip() for span in torrent_category.find_all('span')]

        for link in soup.find_all('a', href=True):
            href_value = link['href']
            if href_value.startswith('magnet:'):
                magnet_links.append(href_value)

        for img in soup.find_all('img',class_='img-responsive descrimg'):
            img_value = img['src']
            if img_value.startswith('https://'):
                images.append(img_value)

        return {
            "title": data.get("title"),
            "link": data.get("link"),
            "seeds": data.get("seeds"),
            "leeches": data.get("leeches"),
            "date": data.get("date"),
            "size": data.get("size"),
            "uploader": data.get("uploader"),
            'title': title,
            'img': images,
            'genres': genres,
            'description': description,
            'magnet_links': magnet_links,
        }

    except Exception as e:
        print("Error: ", e)    