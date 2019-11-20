```bash
pip install scrapy
pip install fake-agent

cd BaiduImageSpider
scrapy crawl spider -o filename.csv
```

Crawled images is under BaiduImageSpider/full

Change search_lists, max_pages in spider/spider.py for your search. According to Baidu Image, each page should contain 30 images.
