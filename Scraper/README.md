# AutoScraper
This is a Scrapy project to scrape price of cars from https://auto.ria.com/newauto/marka-mercedes-benz

This project is my first real experience in scraping. See launch instructions below.

If you don't have Scrapy(https://scrapy.org/) installed. 

let's install it:

```bash
pip install scrapy 
```
# Spiders


This project contains spider and you can list it using the list command:
```scrapy
scrapy startproject name
```

```scrapy
scrapy list
```

# Running the spiders

You can run a spider using the scrapy crawl command, such as:
```scrapy
scrapy crawl ScraperV2 
```
If you want to save the scraped data to a file, you can pass the -o option:
```scrapy
scrapy crawl ScarperV2 -o example.json
```

