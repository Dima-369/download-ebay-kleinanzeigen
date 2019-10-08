import requests
import os
from bs4 import BeautifulSoup
from collections import namedtuple

Page = namedtuple('Page', 'dir url')

pages = [
    Page('desktop',
         'https://www.ebay-kleinanzeigen.de/s-anzeige/...')
]


def main():
    for p in pages:
        try:
            os.mkdir(p.dir)
        except FileExistsError:
            pass

        html = requests.get(p.url).text
        soup = BeautifulSoup(html, 'html.parser')

        images = soup.select_one('#viewad-thumbnail-list')\
            .find_all('img', src=True)
        for i, img in enumerate(images):
            src_url = img['data-imgsrc']
            r = requests.get(src_url)
            with open(f'{p.dir}/{i}.jpg', 'wb') as f:
                f.write(r.content)

        category = soup.select_one('#vap-brdcrmb').text.strip() \
            .replace('\n', ' ')
        title = soup.select_one('#viewad-title').text.strip()
        price = soup.select_one('#viewad-price').text.strip()
        desc = soup.select_one('#viewad-description-text') \
            .get_text(separator='\n').strip()
        with open(f'{p.dir}/desc.txt', 'w') as f:
            final_text = f'{category}\n\n{title}\n{price}\n\n{desc}'
            f.write(final_text)

        print(f'Processed {p.url}')


if __name__ == '__main__':
    main()
