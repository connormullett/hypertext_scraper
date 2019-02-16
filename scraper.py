#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import sys
from tqdm import tqdm


def main(searcher, url):

    def get_links(http_only=False):
        links = []
        for link in tqdm(b.find_all('a')):
            if http_only:
                if link.get('href').startswith('http'):
                    links.append(link.get('href'))
            else:
                links.append(link.get('href'))
        for link in links:
            print(link)
        exit()

    response = requests.get(url)
    b = BeautifulSoup(response.text, features='html.parser')

    scrape_mapper = {
            'text': b.get_text,
            'links': get_links,
            'http-links': get_links
            }

    s = scrape_mapper.get(searcher, None)
    if s == get_links and searcher == 'http-links':
        get_links(True)
    text = s()
    print(text)


if __name__ == '__main__':
    try:
        searcher = sys.argv[1]
        url = sys.argv[2]
        main(searcher, url)
    except IndexError:
        print('Usage: python3 {text/links/http-links} {url}')

