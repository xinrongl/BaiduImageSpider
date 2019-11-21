# BaiduImageSpider
A basic image crawler with fake-agent for baidu search engine.

The purpose of this is to collect image data for image recognization and should not be use for any business purpose.

All crawled images are stored in the /full/search_word

To run the crawler:
```cmd
scrapy crawl spider -o filename.csv
```
Use scrapy >= 0.16.0
