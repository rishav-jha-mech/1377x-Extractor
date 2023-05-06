import json
import time
import requests
from bs4 import BeautifulSoup
from utils import sanitize_filename

SLEEP_TIME = 1
OUTPUT_FOLDER = './outputs/'
ERRORS_FOLDER = './errors/'

def extractSubData(range, option,optionName):
    """
    Extract data from a page
    @params: range, option
    range = range of pages to extract, type => range(start,stop+1)
    option = category of torrent, type => dataListOptions
    """
    for page in range:
        print("Scraping page ...", page)
        response = requests.get(f"https://www.1377x.to/sub/{option}/{page}")
        html = response.content
        soup = BeautifulSoup(html, "html.parser")
        try:
            datas = soup.find_all("table", class_="table")[0]
            rows = soup.find_all("tr")
            results = []

            for i, row in enumerate(rows):
                if i == 0:
                    continue
                title = (
                    row.find("td", class_="coll-1 name").find_all("a")[1].text.strip()
                )
                link = row.find("td", class_="coll-1 name").find_all("a")[1]["href"]
                seeds = int(row.find("td", class_="coll-2 seeds").text.strip())
                leeches = int(row.find("td", class_="coll-3 leeches").text.strip())
                date = row.find("td", class_="coll-date").text.strip()
                size = row.find("td", class_="coll-4 size mob-uploader").text.strip()
                uploader = row.find("td", class_="coll-5 uploader").text.strip()
                results.append(
                    {
                        "title": title,
                        "link": link,
                        "seeds": seeds,
                        "leeches": leeches,
                        "date": date,
                        "size": size,
                        "uploader": uploader,
                    }
                )

            with open(f"{OUTPUT_FOLDER}{sanitize_filename(optionName)}.json", "a") as f:
                json.dump(results, f)
                f.write("\n")
            time.sleep(SLEEP_TIME)
        except Exception as e:
            print("Error on page ...", page, e)
            with open(f"{ERRORS_FOLDER}error-{sanitize_filename(optionName)}-page{page}.html", "w") as f:
                f.write(soup.prettify())
            continue
    print("\nData scraping completed\n")


def extractDataList(range, option,optionName):
    """
    Extract data from a page
    @params: range, option
    range = range of pages to extract, type => range(start,stop+1)
    option = category of torrent, type => dataListOptions
    """
    for page in range:
        print("Scraping page ...", page)
        response = requests.get(f"https://www.1377x.to/cat/{optionName}/{page}")
        html = response.content
        soup = BeautifulSoup(html, "html.parser")
        try:
            results = []
            datas = soup.find_all("table", class_="table")[0]
            rows = soup.find_all("tr")

            for i, row in enumerate(rows):
                if i == 0:
                    continue
                title = (
                    row.find("td", class_="coll-1 name").find_all("a")[1].text.strip()
                )
                link = row.find("td", class_="coll-1 name").find_all("a")[1]["href"]
                seeds = int(row.find("td", class_="coll-2 seeds").text.strip())
                leeches = int(row.find("td", class_="coll-3 leeches").text.strip())
                date = row.find("td", class_="coll-date").text.strip()
                size = row.find("td", class_="coll-4 size mob-uploader").text.strip()
                uploader = row.find("td", class_="coll-5 uploader").text.strip()
                results.append(
                    {
                        "title": title,
                        "link": link,
                        "seeds": seeds,
                        "leeches": leeches,
                        "date": date,
                        "size": size,
                        "uploader": uploader,
                    }
                )

            with open(f"{OUTPUT_FOLDER}{sanitize_filename(optionName)}.json", "a") as f:
                json.dump(results, f)
                f.write("\n")
            time.sleep(SLEEP_TIME)

        except Exception as e:
            print("Error on page ...", page, e)
            with open(f"{ERRORS_FOLDER}error-{sanitize_filename(optionName)}-page{page}.html", "w") as f:
                f.write(soup.prettify())
            continue
    print("\nData scraping completed\n")
