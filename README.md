
# Scraper
## Simple webscraper that grabs text, links, or links starting with http

## Requires
- python3
- (BeautifulSoup)[https://crummy.com/software/beautifulsoup/bs4/doc]
- requests  `pip install requests`

## Usage
`python3 scraper.py {what to scrape} {url}`  

## Where what to scrape can be one of the following
- `text` - grabs all text from webpage
- `links` - grabs all links rendered in DOM, (these dont have to be http)
- `http-links` - grabs all http links

