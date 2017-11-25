import requests
from bs4 import BeautifulSoup
from new2k17 import download_web_image

def trade_spider(max_pages, url='http://boards.4chan.org/b/'):
    page = 1
    while page <= max_pages:
        url = url + str(page)
        if page == 1:
            url = url[:-1]
        source_code = requests.get(url)
        plaine_text = source_code.text
        soup = BeautifulSoup(plaine_text, "html.parser")
        for line in soup.findAll("a", {"class": "replylink"}):
            href = url + line.get('href')
            if len(href) < 43:
                continue
            print(href)
            get_link_images(href)
        page += 1

def get_link_images(item_Link):
    source_code = requests.get(item_Link)
    plain_Text = source_code.text
    soup = BeautifulSoup(plain_Text, "html.parser")
    for link in soup.findAll("a", {'class': 'fileThumb'}):
        scr = 'http:' + link.get('href')
        download_web_image(scr)

if __name__ == '__main__':
    url_addres = input("Enter addres board, where you want download multimedia: ")
    trade_spider(10, url_addres)
