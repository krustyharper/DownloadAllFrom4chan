import random
import urllib.request as D

def download_web_image(url):
    name = random.randrange(1,5000)
    if url.endswith('.webm'):
        full_name = '{0:0^4}'.format(name) + ".webm"
    elif url.endswith('.jpg'):
        full_name = '{0:0^4}'.format(name) + ".jpg"
    elif url.endswith('.png'):
        full_name = '{0:0^4}'.format(name) + ".png"
    elif url.endswith('.gif'):
        full_name = '{0:0^4}'.format(name) + ".gif"
    D.urlretrieve(url, full_name)

if __name__ == '__main__':
    download_web_image('https://i.4cdn.org/b/1502961232157.png')

